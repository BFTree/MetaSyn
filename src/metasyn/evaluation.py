"""Public MetaSyn evaluation contracts and ID-based metrics."""

from __future__ import annotations

import re
import statistics
from collections.abc import Iterable, Mapping, Sequence
from typing import Any

from .rag import extract_included_articles


EVALUATOR_VERSION = "1.2.0"
PROMPT_VERSION = "metasyn-evaluator-2026-07-20"
RESULT_SCHEMA_VERSION = "1.1"

RETRIEVAL_DIAGNOSTIC_NAMES = (
    "retrieval_recall",
    "retrieval_precision",
    "conditional_retention",
    "post_retrieval_loss",
)
PIPELINE_ID_METRIC_NAMES = (
    "inclusion_recall",
    "inclusion_precision",
    "inclusion_f1",
    "screening_accuracy",
)
ID_METRIC_NAMES = RETRIEVAL_DIAGNOSTIC_NAMES + PIPELINE_ID_METRIC_NAMES
TEXT_METRIC_NAMES = (
    "inclusion_consistency",
    "exclusion_consistency",
    "conclusion_direction_accuracy",
    "insights_consistency",
    "structure_quality",
)
MAIN_METRIC_NAMES = PIPELINE_ID_METRIC_NAMES + TEXT_METRIC_NAMES
BENCHMARK_METRIC_NAMES = RETRIEVAL_DIAGNOSTIC_NAMES + MAIN_METRIC_NAMES


class EvaluationInputError(ValueError):
    """Raised when a public result record does not satisfy the evaluator schema."""


def _strict_int(value: Any, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise EvaluationInputError(f"{field} must be an integer")
    if value < 0:
        raise EvaluationInputError(f"{field} must be non-negative")
    return value


def unique_article_ids(value: Any, field: str) -> list[int]:
    """Validate an ordered list of unique corpus article IDs."""
    if not isinstance(value, list):
        raise EvaluationInputError(f"{field} must be a JSON array of integers")
    article_ids = [_strict_int(item, f"{field}[{index}]") for index, item in enumerate(value)]
    if len(article_ids) != len(set(article_ids)):
        raise EvaluationInputError(f"{field} must not contain duplicate article IDs")
    return article_ids


def normalize_unmatched_entries(value: Any) -> list[str]:
    """Validate and deduplicate citations that could not be mapped to the pool."""
    if not isinstance(value, list):
        raise EvaluationInputError(
            "unmatched_included_entries must be a JSON array of non-empty strings"
        )
    entries: list[str] = []
    seen: set[str] = set()
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            raise EvaluationInputError(
                f"unmatched_included_entries[{index}] must be a non-empty string"
            )
        cleaned = re.sub(r"\s+", " ", item).strip()
        key = cleaned.casefold()
        if key not in seen:
            seen.add(key)
            entries.append(cleaned)
    return entries


def validate_review_id(record: Mapping[str, Any]) -> int:
    if "review_id" not in record:
        raise EvaluationInputError("result record is missing required field review_id")
    return _strict_int(record["review_id"], "review_id")


def validate_retrieved_articles(record: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Validate the candidate records required for report-based list parsing."""
    raw_articles = record.get("retrieved_articles")
    if not isinstance(raw_articles, list):
        raise EvaluationInputError(
            "report selection requires retrieved_articles with corpus_id and title"
        )
    articles: list[dict[str, Any]] = []
    ids: list[int] = []
    for index, raw in enumerate(raw_articles):
        if not isinstance(raw, Mapping):
            raise EvaluationInputError(f"retrieved_articles[{index}] must be an object")
        corpus_id = _strict_int(
            raw.get("corpus_id"), f"retrieved_articles[{index}].corpus_id"
        )
        title = raw.get("title")
        if not isinstance(title, str) or not title.strip():
            raise EvaluationInputError(
                f"retrieved_articles[{index}].title must be a non-empty string"
            )
        article = dict(raw)
        article["corpus_id"] = corpus_id
        article["title"] = title.strip()
        article["rank"] = index + 1
        articles.append(article)
        ids.append(corpus_id)
    if len(ids) != len(set(ids)):
        raise EvaluationInputError("retrieved_articles must not contain duplicate corpus IDs")
    declared = record.get("retrieved_article_ids")
    if declared is not None and unique_article_ids(declared, "retrieved_article_ids") != ids:
        raise EvaluationInputError(
            "retrieved_article_ids must exactly match retrieved_articles order"
        )
    return articles


def resolve_selection(
    record: Mapping[str, Any],
    report: str | None,
    selection_source: str,
) -> dict[str, Any]:
    """Resolve the final evidence list from a report or strict structured JSON.

    ``selection_source='report'`` parses exact titles and explicit corpus IDs from
    the report against ``retrieved_articles``. ``selection_source='json'`` uses
    the strict result fields and performs no report-list parsing.
    """
    validate_review_id(record)
    if selection_source == "report":
        if report is None:
            raise EvaluationInputError("report selection requires a report file")
        candidates = validate_retrieved_articles(record)
        parsed = extract_included_articles(report, candidates)
        if not parsed["selection_resolved"]:
            raise EvaluationInputError(
                "the report has no resolvable final included-article list; use a "
                "dedicated list with exact titles or Corpus ID values"
            )
        return {
            "source": "report",
            "retrieved_article_ids": [item["corpus_id"] for item in candidates],
            "included_article_ids": list(parsed["included_article_ids"]),
            "unmatched_included_article_ids": list(
                parsed["unmatched_included_article_ids"]
            ),
            "unmatched_included_entries": normalize_unmatched_entries(
                parsed.get("unmatched_included_entries", [])
            ),
            "parser": {
                key: value
                for key, value in parsed.items()
                if key
                not in {
                    "included_article_ids",
                    "included_articles",
                    "unmatched_included_article_ids",
                    "unmatched_included_entries",
                    "list_text",
                }
            },
        }
    if selection_source != "json":
        raise EvaluationInputError("selection_source must be 'report' or 'json'")

    required = (
        "retrieved_article_ids",
        "included_article_ids",
        "unmatched_included_article_ids",
    )
    missing = [field for field in required if field not in record]
    if missing:
        raise EvaluationInputError(
            "strict JSON selection is missing required fields: " + ", ".join(missing)
        )
    if "unmatched_included_article_count" in record:
        raise EvaluationInputError(
            "unmatched_included_article_count is derived by the evaluator; "
            "supply unmatched_included_article_ids and unmatched_included_entries only"
        )
    retrieved = unique_article_ids(record["retrieved_article_ids"], "retrieved_article_ids")
    included = unique_article_ids(record["included_article_ids"], "included_article_ids")
    outside_pool = sorted(set(included) - set(retrieved))
    if outside_pool:
        raise EvaluationInputError(
            "included_article_ids must be drawn from retrieved_article_ids; put "
            f"unmapped IDs in unmatched_included_article_ids: {outside_pool}"
        )
    unmatched_ids = unique_article_ids(
        record["unmatched_included_article_ids"], "unmatched_included_article_ids"
    )
    mapped_unmatched = sorted(set(unmatched_ids) & set(retrieved))
    if mapped_unmatched:
        raise EvaluationInputError(
            "unmatched_included_article_ids must not contain retrieved corpus IDs: "
            f"{mapped_unmatched}"
        )
    entries = normalize_unmatched_entries(record.get("unmatched_included_entries", []))
    return {
        "source": "json",
        "retrieved_article_ids": retrieved,
        "included_article_ids": included,
        "unmatched_included_article_ids": unmatched_ids,
        "unmatched_included_entries": entries,
    }


def _unmatched_keys(
    article_ids: Iterable[int], entries: Iterable[str]
) -> set[str]:
    keys = {f"corpus id: {int(value)}" for value in article_ids}
    keys.update(
        re.sub(r"\s+", " ", str(value)).strip().casefold()
        for value in entries
        if str(value).strip()
    )
    return keys


def id_metrics(
    reference_article_ids: Iterable[int],
    included_article_ids: Iterable[int],
    retrieved_article_ids: Iterable[int],
    unmatched_included_article_ids: Iterable[int] = (),
    unmatched_included_entries: Iterable[str] = (),
) -> dict[str, float | int | None]:
    """Compute deterministic retrieval and evidence-list metrics for one review."""
    reference = {int(value) for value in reference_article_ids}
    included = {int(value) for value in included_article_ids}
    retrieved = {int(value) for value in retrieved_article_ids}
    unmatched = _unmatched_keys(
        unmatched_included_article_ids, unmatched_included_entries
    )
    predicted_count = len(included) + len(unmatched)
    true_positive = len(reference & included)
    retrieved_reference = reference & retrieved
    retained_reference = retrieved_reference & included
    if not reference:
        retrieval_recall = retrieval_precision = retention = post_loss = None
        recall = precision = f1 = None
    else:
        retrieval_recall = len(retrieved_reference) / len(reference)
        retrieval_precision = (
            len(retrieved_reference) / len(retrieved) if retrieved else 0.0
        )
        retention = (
            len(retained_reference) / len(retrieved_reference)
            if retrieved_reference
            else None
        )
        post_loss = len(retrieved_reference - included) / len(reference)
        if not predicted_count:
            recall = precision = f1 = 0.0
        else:
            recall = true_positive / len(reference)
            precision = true_positive / predicted_count
            f1 = (
                2 * recall * precision / (recall + precision)
                if recall + precision
                else 0.0
            )
    correct = sum(
        (corpus_id in included) == (corpus_id in reference)
        for corpus_id in retrieved
    )
    return {
        "retrieval_recall": (
            round(retrieval_recall, 4) if retrieval_recall is not None else None
        ),
        "retrieval_precision": (
            round(retrieval_precision, 4) if retrieval_precision is not None else None
        ),
        "conditional_retention": (
            round(retention, 4) if retention is not None else None
        ),
        "post_retrieval_loss": (
            round(post_loss, 4) if post_loss is not None else None
        ),
        "inclusion_recall": round(recall, 4) if recall is not None else None,
        "inclusion_precision": round(precision, 4) if precision is not None else None,
        "inclusion_f1": round(f1, 4) if f1 is not None else None,
        "screening_accuracy": round(correct / len(retrieved), 4) if retrieved else 0.0,
        "mapped_included_count": len(included),
        "unmatched_included_article_count": len(unmatched),
    }


def null_text_metrics() -> dict[str, None]:
    return {name: None for name in TEXT_METRIC_NAMES}


def macro_average(
    evaluations: Sequence[Mapping[str, Any]],
    metric_names: Iterable[str] = BENCHMARK_METRIC_NAMES,
) -> tuple[dict[str, float | None], dict[str, int]]:
    """Macro-average per-review metrics and report each valid denominator."""
    means: dict[str, float | None] = {}
    counts: dict[str, int] = {}
    for name in metric_names:
        values = [
            float(item["metrics"][name])
            for item in evaluations
            if isinstance(item.get("metrics", {}).get(name), (int, float))
            and not isinstance(item["metrics"][name], bool)
        ]
        means[name] = round(statistics.fmean(values), 4) if values else None
        counts[name] = len(values)
    return means, counts
