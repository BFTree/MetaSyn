"""Task-scoped search and fetch tools for third-party research agents."""

from __future__ import annotations

import math
from typing import Iterable

from .query import build_protocol_query
from .retrieval import Retriever, candidate_record


def build_agent_prompt(review: dict) -> str:
    def field(name: str) -> str:
        value = review.get(name)
        return "NR" if value in (None, "") else str(value)

    return f"""You are conducting a systematic review and meta-analysis over the local MetaSyn PubMed corpus.

Use the local corpus search tool as the only retrieval source. You must retrieve local corpus records before writing the report. Screen candidate primary studies against the eligibility criteria and preserve exact Corpus ID values from search results.

The retrieval seed below contains the research question and PI/ECO fields. Use it to formulate focused corpus searches; do not search for or infer the title of the source meta-analysis.

Retrieval seed:
{build_protocol_query(review)}

Search start date: {field('search_start_date')}
Search end date: {field('search_end_date')}

Inclusion criteria:
{field('inclusion_criteria')}

Exclusion criteria:
{field('exclusion_criteria')}

Report requirements:
- Report the local corpus search queries used.
- Discuss retrieval, screening, included studies, findings, limitations, and conclusion.
- Mention when evidence is abstract-only because full-text sections are unavailable.
- End with a clearly identified included-article list. Give the title and Corpus ID for each included article, or state that no article was included.
"""


class AgentCorpusTools:
    """Leakage-safe tool layer shared by GPT-Researcher and OpenDR."""

    def __init__(
        self,
        retriever: Retriever,
        review: dict,
        k: int = 20,
        oracle: bool = False,
        search_abstract_chars: int = 4000,
        tool_observation_chars: int | None = None,
        fetch_chars: int = 6000,
        max_distinct_articles: int | None = 200,
    ) -> None:
        self.retriever = retriever
        self.review = review
        self.k = k
        self.oracle = oracle
        self.search_abstract_chars = search_abstract_chars
        self.tool_observation_chars = tool_observation_chars
        self.fetch_chars = fetch_chars
        if max_distinct_articles is not None and max_distinct_articles < 1:
            raise ValueError("max_distinct_articles must be positive or None")
        self.max_distinct_articles = max_distinct_articles
        self.source_ids = {
            int(value) for value in review.get("source_review_corpus_ids") or []
        }
        self.ground_truth_ids = {
            int(value) for value in review.get("matched_corpus_ids") or []
        }
        self.returned_ids: set[int] = set()

    def search(self, query: str) -> list[dict]:
        if self.oracle:
            rows = self.retriever.search_oracle_text(
                query, self.ground_truth_ids, self.source_ids, self.k
            )
        else:
            rows = self.retriever.search_text(query, self.source_ids, self.k)
        visible_rows = []
        for row in rows:
            corpus_id = int(row["corpus_id"])
            already_visible = corpus_id in self.returned_ids
            below_cap = (
                self.max_distinct_articles is None
                or len(self.returned_ids) < self.max_distinct_articles
            )
            if already_visible or below_cap:
                visible_rows.append(row)
                self.returned_ids.add(corpus_id)
        return [
            {
                **row,
                "abstract": (row.get("abstract") or "")[: self.search_abstract_chars],
            }
            for row in visible_rows
        ]

    def search_observation(self, query: str) -> str:
        """Return the search observation, optionally bounded by configuration."""
        rows = self.search(query)
        blocks = [
            "\n".join(
                [
                    f"Corpus ID: {row['corpus_id']}",
                    f"Title: {row.get('title') or 'Not reported'}",
                    f"Year: {row.get('year') or 'Not reported'}",
                    f"Abstract: {row.get('abstract') or 'Not reported'}",
                ]
            )
            for row in rows
        ]
        observation = "\n\n---\n\n".join(blocks)
        if self.tool_observation_chars is None:
            return observation
        return observation[: self.tool_observation_chars]

    def fetch(
        self,
        corpus_id: int,
        section: str = "",
        chunk: int = 0,
        chunk_chars: int | None = None,
    ) -> dict:
        corpus_id = int(corpus_id)
        if corpus_id not in self.returned_ids:
            raise PermissionError("Fetch is allowed only after this task returned the record")
        row = self.retriever.fetch(corpus_id, self.source_ids)
        sections = {
            str(item.get("heading") or "Section"): str(item.get("text") or "")
            for item in row.get("sections") or []
        }
        requested = section.strip()
        if requested.casefold() in {"", "all", "full", "full_text", "fulltext"}:
            pieces = []
            if row.get("abstract"):
                pieces.append(f"## Abstract\n{row['abstract']}")
            pieces.extend(f"## {name}\n{text}" for name, text in sections.items())
            selected = "all"
            text = "\n\n".join(pieces)
        elif requested.casefold() in {"abstract", "summary"}:
            selected = "abstract"
            text = row.get("abstract") or ""
        else:
            matches = [
                name
                for name in sections
                if requested.casefold() == name.casefold()
                or requested.casefold() in name.casefold()
                or name.casefold() in requested.casefold()
            ]
            if not matches:
                return {
                    **candidate_record(row, corpus_id, 0, None),
                    "error": "section_not_found",
                    "requested_section": requested,
                    "available_sections": list(sections),
                }
            selected = matches[0]
            text = sections[selected]
        width = max(1, int(chunk_chars or self.fetch_chars))
        chunk_index = max(0, int(chunk) - 1) if int(chunk) > 0 else 0
        total_chunks = max(1, math.ceil(len(text) / width))
        start = min(chunk_index * width, len(text))
        end = min(start + width, len(text))
        return {
            **candidate_record(row, corpus_id, 0, None),
            "requested_section": requested,
            "fetched_section": selected,
            "available_sections": list(sections),
            "chunk": chunk_index + 1,
            "total_chunks": total_chunks,
            "char_start": start,
            "char_end": end,
            "total_chars": len(text),
            "out_of_range": chunk_index >= total_chunks,
            "content": text[start:end].rstrip(),
        }

    def fetch_observation(
        self, corpus_id: int, section: str = "", chunk: int = 0
    ) -> str:
        row = self.fetch(corpus_id, section, chunk)
        if row.get("error"):
            return (
                f"Corpus ID: {row['corpus_id']}\nError: {row['error']}\n"
                f"Available sections: {', '.join(row['available_sections'])}"
            )
        return "\n".join(
            [
                f"Corpus ID: {row['corpus_id']}",
                f"Title: {row.get('title') or 'Not reported'}",
                f"Year: {row.get('year') or 'Not reported'}",
                row["content"],
            ]
        )
