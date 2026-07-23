"""BM25 baseline used in the MetaSyn retrieval experiments."""

from __future__ import annotations

import re
from typing import Iterable

import numpy as np
from datasets import Dataset
from rank_bm25 import BM25Okapi

from .query import build_protocol_query
from .retrieval import candidate_record


STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
    "this", "that", "these", "those", "it", "its", "as", "also", "can",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "must", "than", "into", "through", "during",
    "before", "after", "above", "below", "between", "under", "again",
    "further", "then", "once", "here", "there", "when", "where", "why",
    "how", "all", "each", "few", "more", "most", "other", "some", "such",
    "no", "nor", "not", "only", "own", "same", "so", "just", "now",
}


def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"\b\w+\b", text.lower())
    return [token for token in tokens if len(token) > 2 and token not in STOPWORDS]


class BM25Retriever:
    """In-memory BM25Okapi baseline over title and abstract."""

    def __init__(self, corpus: Dataset) -> None:
        self.corpus = corpus
        self.documents = [
            tokenize(f"{row.get('title') or ''} {row.get('abstract') or ''}")
            for row in corpus
        ]
        self.index = BM25Okapi(self.documents)

    def search(
        self,
        review: dict,
        k: int = 200,
        additional_excluded_ids: Iterable[int] = (),
    ) -> list[dict]:
        excluded = {
            int(value) for value in review.get("source_review_corpus_ids") or []
        }
        excluded.update(int(value) for value in additional_excluded_ids)
        scores = self.index.get_scores(tokenize(build_protocol_query(review)))
        for position, corpus_id in enumerate(self.corpus["ID"]):
            if int(corpus_id) in excluded:
                scores[position] = -np.inf
        positions = scores.argsort()[::-1]
        output = []
        for position in positions:
            if len(output) == k or scores[position] <= 0:
                break
            row = dict(self.corpus[int(position)])
            output.append(
                candidate_record(
                    row, int(row["ID"]), len(output) + 1, float(scores[position])
                )
            )
        return output

