"""Evaluator-dependent MetaSyn metrics using the released final prompts."""

from __future__ import annotations

import numpy as np
from sentence_transformers import SentenceTransformer

from .llm_client import LLMClient


class OpenAIJudge(LLMClient):
    """Public name for the final OpenAI-compatible evaluator client."""


class CriteriaSimilarity:
    def __init__(
        self,
        model_name: str = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
    ) -> None:
        self.model = SentenceTransformer(model_name)

    def soft_f1(self, reference: list[str], predicted: list[str]) -> float:
        if not reference or not predicted:
            return 0.0
        left = self.model.encode(reference, normalize_embeddings=True)
        right = self.model.encode(predicted, normalize_embeddings=True)
        similarities = np.asarray(left) @ np.asarray(right).T
        recall = float(similarities.max(axis=1).mean())
        precision = float(similarities.max(axis=0).mean())
        return round(
            2 * recall * precision / (recall + precision)
            if recall + precision
            else 0.0,
            4,
        )


def _criteria_items(value: str | None) -> list[str]:
    return [item.strip() for item in (value or "").split(";") if item.strip()]


def validate_reference_direction(value: object) -> str | None:
    """Validate the released three-class conclusion-direction contract."""
    if value in (None, "NR"):
        return None
    if value not in {"Positive", "Negative", "Mixed"}:
        raise ValueError(
            "Effect_Direction must be Positive, Negative, Mixed, or NR; "
            f"received {value!r}"
        )
    return str(value)


def text_metrics(
    report: str,
    review: dict,
    judge: OpenAIJudge,
    similarity: CriteriaSimilarity | None = None,
) -> dict:
    """Compute the final per-review evaluator-dependent metrics."""
    reference_direction = validate_reference_direction(review.get("Effect_Direction"))
    inclusion, exclusion = judge.extract_criteria(report)
    direction, insights = judge.extract_conclusion_and_insights(report)
    similarity = similarity or CriteriaSimilarity()
    metrics = {}

    reference_inclusion = review.get("inclusion_criteria")
    if reference_inclusion is None:
        metrics["inclusion_consistency"] = None
        metrics["inclusion_consistency_skipped"] = True
    else:
        items = _criteria_items(reference_inclusion)
        metrics["inclusion_consistency"] = (
            similarity.soft_f1(items, inclusion) if items and inclusion else 0.0
        )
        metrics["inclusion_consistency_skipped"] = False

    reference_exclusion = review.get("exclusion_criteria")
    if reference_exclusion is None:
        metrics["exclusion_consistency"] = None
        metrics["exclusion_consistency_skipped"] = True
    else:
        items = _criteria_items(reference_exclusion)
        metrics["exclusion_consistency"] = (
            similarity.soft_f1(items, exclusion) if items and exclusion else 0.0
        )
        metrics["exclusion_consistency_skipped"] = False

    if reference_direction is None:
        metrics["conclusion_direction_accuracy"] = None
        metrics["conclusion_direction_skipped"] = True
    else:
        metrics["conclusion_direction_accuracy"] = int(direction == reference_direction)
        metrics["conclusion_direction_skipped"] = False

    reference_insights = review.get("Key_Insights") or ""
    if not reference_insights:
        metrics["insights_consistency"] = None
        metrics["insights_consistency_skipped"] = True
    elif not insights:
        metrics["insights_consistency"] = 0.0
        metrics["insights_consistency_skipped"] = False
    else:
        score = judge.evaluate_insights_consistency(insights, reference_insights)
        metrics["insights_consistency"] = round(score, 4)
        metrics["insights_consistency_skipped"] = False

    structure, reason = judge.evaluate_structure_quality(report)
    metrics["structure_quality"] = round(structure, 2)
    metrics["structure_quality_reason"] = reason
    metrics["extracted"] = {
        "inclusion_criteria": inclusion,
        "exclusion_criteria": exclusion,
        "conclusion_direction": direction,
        "key_insights": insights,
    }
    return metrics
