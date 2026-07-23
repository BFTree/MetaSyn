#!/usr/bin/env python3
"""Evaluate one complete 86-review MetaSyn test run and macro-average metrics."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from metasyn.data import load_reviews
from metasyn.evaluation import (
    BENCHMARK_METRIC_NAMES,
    ID_METRIC_NAMES,
    macro_average,
)
from metasyn.evaluator import evaluate_record, evaluator_metadata
from metasyn.judge import CriteriaSimilarity, OpenAIJudge, validate_reference_direction


def load_records(results_dir: Path) -> dict[int, tuple[dict, Path]]:
    paths = sorted(results_dir.rglob("results.json"))
    if not paths:
        raise ValueError(f"no results.json files found under {results_dir}")
    records: dict[int, tuple[dict, Path]] = {}
    for path in paths:
        record = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(record, dict):
            raise ValueError(f"{path} must contain one JSON object")
        review_id = record.get("review_id")
        if isinstance(review_id, bool) or not isinstance(review_id, int):
            raise ValueError(f"{path} has no integer review_id")
        if review_id in records:
            raise ValueError(
                f"duplicate review_id {review_id}: {records[review_id][1]} and {path}"
            )
        records[review_id] = (record, path)
    return records


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--dataset", default="THUIR/MetaSyn")
    parser.add_argument("--dataset-revision")
    parser.add_argument("--judge-model")
    parser.add_argument("--id-only", action="store_true")
    parser.add_argument(
        "--selection-source", choices=("report", "json"), default="report"
    )
    args = parser.parse_args()

    reviews = {
        int(row["ID"]): dict(row)
        for row in load_reviews("test", args.dataset, args.dataset_revision)
    }
    if len(reviews) != 86:
        raise RuntimeError(f"expected 86 released test reviews, found {len(reviews)}")
    for review in reviews.values():
        validate_reference_direction(review.get("Effect_Direction"))

    records = load_records(args.results_dir)
    expected_ids = set(reviews)
    submitted_ids = set(records)
    missing = sorted(expected_ids - submitted_ids)
    extra = sorted(submitted_ids - expected_ids)
    if missing or extra:
        raise RuntimeError(
            f"test coverage mismatch: missing={missing or 'none'}, extra={extra or 'none'}"
        )

    # Keep deterministic metrics available even when an optional judge
    # dependency or API credential is unavailable. Each review then receives an
    # explicit failed text-evaluation record instead of aborting the whole batch.
    judge = None
    similarity = None
    if not args.id_only:
        try:
            judge = OpenAIJudge(model=args.judge_model)
        except Exception:
            judge = None
        try:
            similarity = CriteriaSimilarity()
        except Exception:
            similarity = None
    evaluations = []
    for review_id in sorted(expected_ids):
        record, result_path = records[review_id]
        report_path = result_path.with_name("report.md")
        report_required = args.selection_source == "report" or not args.id_only
        if report_required and not report_path.exists():
            raise FileNotFoundError(f"missing report for review {review_id}: {report_path}")
        report = report_path.read_text(encoding="utf-8") if report_path.exists() else None
        evaluations.append(
            evaluate_record(
                record,
                reviews[review_id],
                report,
                selection_source=args.selection_source,
                dataset_id=args.dataset,
                dataset_revision=args.dataset_revision,
                judge=judge,
                judge_model=args.judge_model,
                similarity=similarity,
                id_only=args.id_only,
            )
        )

    failed = [item for item in evaluations if item["status"] != "succeeded"]
    metric_names = ID_METRIC_NAMES if args.id_only else BENCHMARK_METRIC_NAMES
    means, counts = macro_average(evaluations, metric_names)
    metadata = evaluator_metadata(
        dataset_id=args.dataset,
        dataset_revision=args.dataset_revision,
        selection_source=args.selection_source,
        judge_model=judge.model if judge is not None else None,
        id_only=args.id_only,
    )
    payload = {
        "status": "failed" if failed else "succeeded",
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
        "evaluator": metadata,
        "coverage": {
            "expected_reviews": 86,
            "submitted_reviews": len(records),
            "succeeded_reviews": len(evaluations) - len(failed),
            "failed_reviews": len(failed),
        },
        "macro_metrics": means if not failed else None,
        "metric_counts": counts if not failed else None,
        "per_review": evaluations,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
