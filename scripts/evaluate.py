#!/usr/bin/env python3
"""Evaluate one MetaSyn report with a traceable public result contract."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv

from metasyn.data import review_by_id
from metasyn.evaluation import ID_METRIC_NAMES, TEXT_METRIC_NAMES
from metasyn.evaluator import evaluate_record, evaluator_metadata


def read_report(path: Path | None, required: bool) -> str | None:
    if path is None or not path.exists():
        if required:
            raise FileNotFoundError(
                "report.md is required for report parsing and evaluator-dependent metrics"
            )
        return None
    return path.read_text(encoding="utf-8")


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--dataset", default="THUIR/MetaSyn")
    parser.add_argument("--dataset-revision")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--judge-model")
    parser.add_argument("--id-only", action="store_true")
    parser.add_argument(
        "--selection-source",
        choices=("report", "json"),
        default="report",
        help="Parse the final list from report.md or use the strict JSON fields",
    )
    args = parser.parse_args()

    payload = None
    review_id = None
    try:
        record = json.loads(args.result.read_text(encoding="utf-8"))
        if not isinstance(record, dict):
            raise ValueError("result must contain one JSON object")
        review_id = record.get("review_id")
        report_path = args.report or args.result.with_name("report.md")
        report = read_report(
            report_path,
            required=args.selection_source == "report" or not args.id_only,
        )
        review = review_by_id(
            int(review_id), args.dataset, revision=args.dataset_revision
        )
        payload = evaluate_record(
            record,
            review,
            report,
            selection_source=args.selection_source,
            dataset_id=args.dataset,
            dataset_revision=args.dataset_revision,
            judge_model=args.judge_model,
            id_only=args.id_only,
        )
    except Exception as exc:
        metric_names = ID_METRIC_NAMES if args.id_only else ID_METRIC_NAMES + TEXT_METRIC_NAMES
        payload = {
            "status": "failed",
            "evaluated_at": datetime.now(timezone.utc).isoformat(),
            "review_id": review_id,
            "evaluator": evaluator_metadata(
                dataset_id=args.dataset,
                dataset_revision=args.dataset_revision,
                selection_source=args.selection_source,
                judge_model=args.judge_model,
                id_only=args.id_only,
            ),
            "metrics": {name: None for name in metric_names},
            "judge_usage": [],
            "error": {"type": type(exc).__name__, "message": str(exc)},
        }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    if payload["status"] != "succeeded":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
