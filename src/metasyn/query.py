"""Canonical MetaSyn query and prompt inputs."""

from __future__ import annotations

from typing import Any


QUERY_PREFIX = "Represent this sentence for searching relevant passages: "


def _value(row: dict[str, Any], key: str) -> str:
    value = row.get(key)
    return "" if value in (None, "", "NR") else str(value).strip()


def build_protocol_query(review: dict[str, Any]) -> str:
    """Build the query used by all fixed-pool retrievers.

    The source-review title is deliberately excluded.
    """
    fields = [
        ("Research Question", _value(review, "Research_Question")),
        ("Population", _value(review, "Population")),
        (
            "Intervention or Exposure",
            _value(review, "Intervention") or _value(review, "Exposure"),
        ),
        ("Comparison", _value(review, "Comparison")),
        ("Outcome", _value(review, "Outcome")),
    ]
    return ". ".join(f"{name}: {value}" for name, value in fields if value)


def retrieval_query(review: dict[str, Any]) -> str:
    return QUERY_PREFIX + build_protocol_query(review)

