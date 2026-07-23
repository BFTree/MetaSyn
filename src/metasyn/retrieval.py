"""MA-Retriever index construction and leakage-safe search."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

import faiss
import numpy as np
from datasets import Dataset
from sentence_transformers import SentenceTransformer

from .query import QUERY_PREFIX, retrieval_query


DEFAULT_MODEL = "BFTree/MA-Retriever"


def document_text(row: dict) -> str:
    return f"Title: {row.get('title') or ''}. Abstract: {row.get('abstract') or ''}"


def candidate_record(
    row: dict, corpus_id: int, rank: int, score: float | None = None
) -> dict:
    """Return the title-and-abstract record exposed by a search call."""
    return {
        "corpus_id": int(corpus_id),
        "rank": int(rank),
        "score": score,
        "pmid": row.get("pmid"),
        "pmc_id": row.get("pmc_id"),
        "doi": row.get("doi"),
        "title": row.get("title") or "",
        "abstract": row.get("abstract") or "",
        "authors": row.get("authors") or [],
        "journal": row.get("journal"),
        "year": row.get("year"),
    }


def build_index(
    corpus: Dataset,
    output: str | Path,
    model_name: str = DEFAULT_MODEL,
    batch_size: int = 128,
    device: str | None = None,
) -> Path:
    """Encode the public corpus and write an ID-mapped HNSW index."""
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    model = SentenceTransformer(model_name, device=device)
    model.max_seq_length = 512
    embeddings = model.encode(
        [document_text(row) for row in corpus],
        batch_size=batch_size,
        normalize_embeddings=True,
        convert_to_numpy=True,
        show_progress_bar=True,
    ).astype(np.float32)
    ids = np.asarray([int(row["ID"]) for row in corpus], dtype=np.int64)
    index = faiss.IndexHNSWFlat(embeddings.shape[1], 32, faiss.METRIC_INNER_PRODUCT)
    index.hnsw.efConstruction = 200
    index.hnsw.efSearch = 512
    index.add(embeddings)
    faiss.write_index(index, str(output / "index.faiss"))
    np.save(output / "corpus_ids.npy", ids)
    (output / "metadata.json").write_text(
        json.dumps(
            {
                "model": model_name,
                "corpus_size": len(corpus),
                "dimension": embeddings.shape[1],
                "normalized": True,
                "query_prefix": "Represent this sentence for searching relevant passages: ",
                "document_template": "Title + Abstract",
                "index": "IndexHNSWFlat",
                "hnsw_m": 32,
                "hnsw_ef_construction": 200,
                "hnsw_ef_search": 512,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return output


class Retriever:
    """Search an ID-mapped MA-Retriever index over the public corpus."""

    def __init__(
        self,
        corpus: Dataset,
        index_dir: str | Path,
        model_name: str = DEFAULT_MODEL,
        device: str | None = None,
    ) -> None:
        self.corpus = corpus
        self.positions = {
            int(corpus_id): position
            for position, corpus_id in enumerate(corpus["ID"])
        }
        self.index = faiss.read_index(str(Path(index_dir) / "index.faiss"))
        self.index_ids = np.load(Path(index_dir) / "corpus_ids.npy")
        if len(self.index_ids) != self.index.ntotal:
            raise RuntimeError("Index and corpus ID mapping have different sizes")
        self.index_positions = {
            int(corpus_id): position
            for position, corpus_id in enumerate(self.index_ids)
        }
        self.model = SentenceTransformer(model_name, device=device)
        self.model.max_seq_length = 512

    def _search_text(
        self,
        query: str,
        k: int,
        excluded: set[int],
        initial_candidate_k: int = 512,
        dynamic_ef_search: bool = True,
    ) -> list[dict]:
        if k < 1:
            raise ValueError("k must be positive")
        query = query if query.startswith(QUERY_PREFIX) else QUERY_PREFIX + query
        embedding = self.model.encode(
            [query],
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False,
        ).astype(np.float32)
        search_k = min(self.index.ntotal, initial_candidate_k)
        while True:
            if hasattr(self.index, "hnsw"):
                self.index.hnsw.efSearch = (
                    max(512, min(search_k * 2, 8192))
                    if dynamic_ef_search
                    else 64
                )
            scores, ids = self.index.search(embedding, search_k)
            kept = [
                (int(self.index_ids[int(position)]), float(score))
                for position, score in zip(ids[0], scores[0])
                if position >= 0
                and int(self.index_ids[int(position)]) not in excluded
            ]
            if len(kept) >= k or search_k == self.index.ntotal:
                break
            if search_k >= min(self.index.ntotal, 8192):
                raise RuntimeError("Cannot obtain enough eligible records from 8192 candidates")
            search_k = min(self.index.ntotal, search_k * 2, 8192)
        results = []
        for rank, (corpus_id, score) in enumerate(kept[:k], start=1):
            row = dict(self.corpus[self.positions[corpus_id]])
            results.append(candidate_record(row, corpus_id, rank, score))
        if len(results) != min(k, self.index.ntotal - len(excluded)):
            raise RuntimeError("The index did not return enough eligible records")
        return results

    def search(
        self,
        review: dict,
        k: int = 200,
        additional_excluded_ids: Iterable[int] = (),
    ) -> list[dict]:
        """Search a review protocol, excluding source records before top-K."""
        excluded = {
            int(value) for value in review.get("source_review_corpus_ids") or []
        }
        excluded.update(int(value) for value in additional_excluded_ids)
        return self._search_text(retrieval_query(review), k, excluded)

    def search_text(
        self, query: str, source_review_ids: Iterable[int], k: int = 20
    ) -> list[dict]:
        """Search an agent-generated query with the same leakage policy."""
        return self._search_text(
            query,
            k,
            {int(value) for value in source_review_ids},
            initial_candidate_k=max(k * 10, 200),
            dynamic_ef_search=False,
        )

    def search_oracle(self, review: dict, k: int = 200) -> list[dict]:
        """Score all task references, place them first, then fill normally."""
        return self.search_oracle_text(
            retrieval_query(review),
            review.get("matched_corpus_ids") or [],
            review.get("source_review_corpus_ids") or [],
            k,
        )

    def fetch(self, corpus_id: int, source_review_ids: Iterable[int] = ()) -> dict:
        """Fetch one corpus record while preventing access to the source review."""
        excluded = {int(value) for value in source_review_ids}
        if int(corpus_id) in excluded:
            raise PermissionError("The source-review record cannot be fetched")
        return dict(self.corpus[self.positions[int(corpus_id)]])

    def search_oracle_text(
        self,
        query: str,
        ground_truth_ids: Iterable[int],
        source_review_ids: Iterable[int],
        k: int = 20,
    ) -> list[dict]:
        """Score all task references for one agent query, then fill normally."""
        source_ids = {int(value) for value in source_review_ids}
        valid_ground_truth = [
            int(value)
            for value in ground_truth_ids
            if int(value) in self.positions and int(value) not in source_ids
        ]
        query_text = query if query.startswith(QUERY_PREFIX) else QUERY_PREFIX + query
        embedding = self.model.encode(
            [query_text], normalize_embeddings=True, convert_to_numpy=True,
            show_progress_bar=False,
        ).astype(np.float32)[0]
        scored = []
        for corpus_id in valid_ground_truth:
            index_position = self.index_positions[corpus_id]
            vector = np.asarray(self.index.reconstruct(index_position), dtype=np.float32)
            scored.append((float(vector @ embedding), corpus_id))
        scored.sort(key=lambda item: (-item[0], item[1]))
        oracle_ids = [corpus_id for _, corpus_id in scored[:k]]
        normal_by_id = {}
        if len(oracle_ids) < k:
            normal_k = max(k, k + len(valid_ground_truth))
            normal = self._search_text(
                query,
                normal_k,
                source_ids | set(valid_ground_truth),
                initial_candidate_k=max(normal_k * 10, 200),
                dynamic_ef_search=False,
            )
            normal_by_id = {int(row["corpus_id"]): row for row in normal}
            oracle_ids.extend(
                int(row["corpus_id"])
                for row in normal
                if len(oracle_ids) < k
            )
        scores = dict((corpus_id, score) for score, corpus_id in scored)
        return [
            candidate_record(
                self.fetch(corpus_id, source_ids),
                corpus_id,
                rank,
                scores.get(corpus_id, normal_by_id.get(corpus_id, {}).get("score")),
            )
            for rank, corpus_id in enumerate(oracle_ids, start=1)
        ]
