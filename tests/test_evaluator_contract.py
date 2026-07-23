import json
from unittest.mock import patch

import pytest

from metasyn.evaluation import (
    BENCHMARK_METRIC_NAMES,
    EvaluationInputError,
    MAIN_METRIC_NAMES,
    RETRIEVAL_DIAGNOSTIC_NAMES,
    id_metrics,
    macro_average,
    resolve_selection,
)
from metasyn.evaluator import evaluate_record
from metasyn.judge import validate_reference_direction
from metasyn.llm_client import JudgeError, LLMClient


def article(corpus_id, title):
    return {"corpus_id": corpus_id, "title": title}


def test_report_selection_parses_titles_ids_and_unmatched_ids():
    record = {
        "review_id": 7,
        "retrieved_article_ids": [11, 12],
        "retrieved_articles": [
            article(11, "Prospective evaluation of treatment recovery in adults"),
            article(12, "Unrelated trial in children"),
        ],
    }
    report = """## Final included articles
- Prospective evaluation of treatment recovery in adults
- Corpus ID: 999999
"""
    selection = resolve_selection(record, report, "report")
    assert selection["included_article_ids"] == [11]
    assert selection["unmatched_included_article_ids"] == [999999]
    metrics = id_metrics(
        [11, 12],
        selection["included_article_ids"],
        selection["retrieved_article_ids"],
        selection["unmatched_included_article_ids"],
    )
    assert metrics["inclusion_recall"] == 0.5
    assert metrics["inclusion_precision"] == 0.5


def test_report_selection_counts_an_unmapped_title_entry():
    record = {
        "review_id": 7,
        "retrieved_article_ids": [11],
        "retrieved_articles": [
            article(11, "Prospective evaluation of treatment recovery in adults")
        ],
    }
    report = """## Final included articles
- A separate trial that is not in the candidate pool
"""
    selection = resolve_selection(record, report, "report")
    assert selection["included_article_ids"] == []
    assert selection["unmatched_included_entries"] == [
        "A separate trial that is not in the candidate pool"
    ]
    metrics = id_metrics(
        [11],
        selection["included_article_ids"],
        selection["retrieved_article_ids"],
        selection["unmatched_included_article_ids"],
        selection["unmatched_included_entries"],
    )
    assert metrics["inclusion_precision"] == 0.0
    assert metrics["unmatched_included_article_count"] == 1


def test_strict_json_derives_unmatched_count_from_unique_entries():
    record = {
        "review_id": 7,
        "retrieved_article_ids": [11, 12],
        "included_article_ids": [11],
        "unmatched_included_article_ids": [999999],
        "unmatched_included_entries": ["Unknown Trial", " unknown   trial "],
    }
    selection = resolve_selection(record, None, "json")
    metrics = id_metrics(
        [11, 12],
        selection["included_article_ids"],
        selection["retrieved_article_ids"],
        selection["unmatched_included_article_ids"],
        selection["unmatched_included_entries"],
    )
    assert metrics["unmatched_included_article_count"] == 2
    assert metrics["inclusion_precision"] == 0.3333


def test_strict_json_rejects_a_caller_supplied_unmatched_count():
    record = {
        "review_id": 7,
        "retrieved_article_ids": [11],
        "included_article_ids": [11],
        "unmatched_included_article_ids": [],
        "unmatched_included_entries": [],
        "unmatched_included_article_count": 0,
    }
    with pytest.raises(EvaluationInputError, match="derived by the evaluator"):
        resolve_selection(record, None, "json")


def test_strict_json_rejects_included_id_outside_retrieved_pool():
    record = {
        "review_id": 7,
        "retrieved_article_ids": [11],
        "included_article_ids": [12],
        "unmatched_included_article_ids": [],
    }
    with pytest.raises(EvaluationInputError, match="drawn from retrieved"):
        resolve_selection(record, None, "json")


def test_direction_contract_rejects_non_public_label():
    assert validate_reference_direction("Mixed") == "Mixed"
    assert validate_reference_direction("NR") is None
    with pytest.raises(ValueError, match="Effect_Direction"):
        validate_reference_direction("Null")


def test_judge_exhaustion_is_an_explicit_failure():
    client = LLMClient.__new__(LLMClient)
    client.max_retries = 2
    client.usage_events = []
    with patch.object(client, "_call", return_value="not json"):
        with pytest.raises(JudgeError, match="failed after 2 attempts"):
            client._call_with_retry("prompt")


def test_macro_average_reports_metric_denominators():
    evaluations = [
        {"metrics": {"inclusion_recall": 0.5}},
        {"metrics": {"inclusion_recall": 1.0}},
        {"metrics": {"inclusion_recall": None}},
    ]
    means, counts = macro_average(evaluations, ["inclusion_recall"])
    assert means == {"inclusion_recall": 0.75}
    assert counts == {"inclusion_recall": 2}


def test_retrieval_diagnostics_use_explicit_denominators():
    metrics = id_metrics(
        [1, 2, 3, 4],
        [1, 5],
        [1, 2, 5, 6],
    )
    assert metrics["retrieval_recall"] == 0.5
    assert metrics["retrieval_precision"] == 0.5
    assert metrics["conditional_retention"] == 0.5
    assert metrics["post_retrieval_loss"] == 0.25
    assert metrics["inclusion_recall"] == 0.25
    assert metrics["inclusion_precision"] == 0.5


def test_retention_is_null_without_a_retrieved_reference():
    metrics = id_metrics([1, 2], [], [3, 4])
    assert metrics["retrieval_recall"] == 0.0
    assert metrics["retrieval_precision"] == 0.0
    assert metrics["conditional_retention"] is None
    assert metrics["post_retrieval_loss"] == 0.0


def test_batch_metric_contract_adds_diagnostics_without_changing_main_metrics():
    assert len(RETRIEVAL_DIAGNOSTIC_NAMES) == 4
    assert len(MAIN_METRIC_NAMES) == 9
    assert BENCHMARK_METRIC_NAMES == RETRIEVAL_DIAGNOSTIC_NAMES + MAIN_METRIC_NAMES


def test_strict_schema_example_is_valid_json():
    example = """{
      "review_id": 63,
      "retrieved_article_ids": [101, 102],
      "included_article_ids": [101],
      "unmatched_included_article_ids": [],
      "unmatched_included_entries": []
    }"""
    selection = resolve_selection(json.loads(example), None, "json")
    assert selection["included_article_ids"] == [101]


class FakeJudge:
    model = "judge-model"

    def __init__(self, fail=False):
        self.fail = fail
        self.usage_events = []

    def extract_criteria(self, report):
        if self.fail:
            raise JudgeError("API unavailable")
        return ["Adults"], ["Animal studies"]

    def extract_conclusion_and_insights(self, report):
        return "Positive", ["Treatment improves recovery in adults."]

    def evaluate_insights_consistency(self, extracted, reference):
        return 0.8

    def evaluate_structure_quality(self, report):
        return 4.0, "Clear sections"


class FakeSimilarity:
    def soft_f1(self, reference, predicted):
        return 0.75


def evaluation_fixture():
    record = {
        "review_id": 7,
        "retrieved_article_ids": [11, 12],
        "included_article_ids": [11],
        "unmatched_included_article_ids": [],
    }
    review = {
        "ID": 7,
        "matched_corpus_ids": [11, 12],
        "inclusion_criteria": "Adults",
        "exclusion_criteria": "Animal studies",
        "Effect_Direction": "Positive",
        "Key_Insights": "Treatment improves recovery in adults.",
    }
    return record, review


def test_complete_evaluation_records_all_nine_metrics_and_provenance():
    record, review = evaluation_fixture()
    payload = evaluate_record(
        record,
        review,
        "## Conclusion\nTreatment improves recovery in adults.",
        selection_source="json",
        dataset_id="THUIR/MetaSyn",
        dataset_revision="abc123",
        judge=FakeJudge(),
        similarity=FakeSimilarity(),
    )
    assert payload["status"] == "succeeded"
    assert payload["metrics"]["inclusion_recall"] == 0.5
    assert payload["metrics"]["inclusion_consistency"] == 0.75
    assert payload["metrics"]["insights_consistency"] == 0.8
    assert payload["metrics"]["structure_quality"] == 4.0
    assert payload["evaluator"]["judge_model"] == "judge-model"
    assert payload["evaluator"]["dataset_revision"] == "abc123"
    assert payload["report_sha256"]


def test_judge_failure_returns_null_text_metrics_and_failed_status():
    record, review = evaluation_fixture()
    payload = evaluate_record(
        record,
        review,
        "report",
        selection_source="json",
        dataset_id="THUIR/MetaSyn",
        judge=FakeJudge(fail=True),
        similarity=FakeSimilarity(),
    )
    assert payload["status"] == "failed"
    assert payload["metrics"]["inclusion_recall"] == 0.5
    assert payload["metrics"]["inclusion_consistency"] is None
    assert payload["metrics"]["structure_quality"] is None
    assert payload["error"]["type"] == "JudgeError"


def test_judge_configuration_failure_preserves_id_metrics():
    record, review = evaluation_fixture()
    with patch(
        "metasyn.evaluator.OpenAIJudge",
        side_effect=RuntimeError("OPENAI_API_KEY is required"),
    ):
        payload = evaluate_record(
            record,
            review,
            "report",
            selection_source="json",
            dataset_id="THUIR/MetaSyn",
            judge_model="judge-model",
        )
    assert payload["status"] == "failed"
    assert payload["metrics"]["inclusion_recall"] == 0.5
    assert payload["metrics"]["inclusion_consistency"] is None
    assert payload["evaluator"]["judge_model"] == "judge-model"
    assert payload["error"]["type"] == "RuntimeError"


def test_report_selection_normalizes_unmatched_title_entries():
    record = {
        "review_id": 7,
        "retrieved_article_ids": [11],
        "retrieved_articles": [article(11, "A known candidate article title")],
    }
    report = "## Final included articles\n- An  unknown   citation   title\n"
    selection = resolve_selection(record, report, "report")
    assert selection["unmatched_included_entries"] == ["An unknown citation title"]
