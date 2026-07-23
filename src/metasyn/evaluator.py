"""End-to-end public evaluator for one MetaSyn review."""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from typing import Any, Mapping

from .evaluation import (
    EVALUATOR_VERSION,
    PROMPT_VERSION,
    RESULT_SCHEMA_VERSION,
    id_metrics,
    null_text_metrics,
    resolve_selection,
    validate_review_id,
)
from .judge import CriteriaSimilarity, OpenAIJudge, text_metrics, validate_reference_direction


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _sha256(text: str | None) -> str | None:
    return hashlib.sha256(text.encode("utf-8")).hexdigest() if text is not None else None


def evaluator_metadata(
    *,
    dataset_id: str,
    dataset_revision: str | None,
    selection_source: str,
    judge_model: str | None,
    id_only: bool,
) -> dict[str, Any]:
    return {
        "evaluator_version": EVALUATOR_VERSION,
        "prompt_version": PROMPT_VERSION,
        "result_schema_version": RESULT_SCHEMA_VERSION,
        "dataset_id": dataset_id,
        "dataset_revision": dataset_revision or "default",
        "selection_source": selection_source,
        "judge_model": None if id_only else judge_model,
        "id_only": id_only,
    }


def evaluate_record(
    record: Mapping[str, Any],
    review: Mapping[str, Any],
    report: str | None,
    *,
    selection_source: str,
    dataset_id: str,
    dataset_revision: str | None = None,
    judge: OpenAIJudge | None = None,
    judge_model: str | None = None,
    similarity: CriteriaSimilarity | None = None,
    id_only: bool = False,
) -> dict[str, Any]:
    """Evaluate one record and return a traceable success or failure payload."""
    review_id = validate_review_id(record)
    if int(review.get("ID")) != review_id:
        raise ValueError(
            f"result review_id {review_id} does not match loaded review {review.get('ID')}"
        )
    validate_reference_direction(review.get("Effect_Direction"))
    selection = resolve_selection(record, report, selection_source)
    metrics = id_metrics(
        review.get("matched_corpus_ids") or [],
        selection["included_article_ids"],
        selection["retrieved_article_ids"],
        selection["unmatched_included_article_ids"],
        selection["unmatched_included_entries"],
    )
    active_judge = judge
    model_name = active_judge.model if active_judge is not None else judge_model
    metadata = evaluator_metadata(
        dataset_id=dataset_id,
        dataset_revision=dataset_revision,
        selection_source=selection_source,
        judge_model=model_name,
        id_only=id_only,
    )
    payload: dict[str, Any] = {
        "status": "succeeded",
        "evaluated_at": _now(),
        "review_id": review_id,
        "report_sha256": _sha256(report),
        "evaluator": metadata,
        "selection": selection,
        "metrics": metrics,
        "judge_usage": [],
    }
    if id_only:
        return payload
    usage_start = 0
    try:
        if active_judge is None:
            active_judge = OpenAIJudge(model=judge_model)
        payload["evaluator"]["judge_model"] = active_judge.model
        usage_start = len(active_judge.usage_events)
        metrics.update(
            text_metrics(
                report or "",
                review,
                active_judge,
                similarity=similarity,
            )
        )
    except Exception as exc:
        metrics.update(null_text_metrics())
        payload["status"] = "failed"
        payload["error"] = {
            "type": type(exc).__name__,
            "message": str(exc),
        }
    payload["evaluated_at"] = _now()
    if active_judge is not None:
        payload["judge_usage"] = list(active_judge.usage_events[usage_start:])
    return payload
