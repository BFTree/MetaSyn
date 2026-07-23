import os
from unittest.mock import MagicMock, patch

from metasyn.query import build_protocol_query
from metasyn.rag import build_prompt, create_client, extract_included_articles
from metasyn.evaluation import id_metrics
from metasyn.agent_tools import AgentCorpusTools
from metasyn.retrieval import Retriever
from metasyn.sparse import BM25Retriever


REVIEW = {
    "ID": 7,
    "Title": "Private source-review title",
    "Research_Question": "Does treatment improve recovery?",
    "Population": "Adults",
    "Intervention": "Treatment",
    "Exposure": None,
    "Comparison": "Usual care",
    "Outcome": "Recovery",
    "source_review_corpus_ids": [10],
    "matched_corpus_ids": [11, 12],
}


def candidate(corpus_id, rank, title):
    return {
        "ID": corpus_id,
        "corpus_id": corpus_id,
        "rank": rank,
        "title": title,
        "abstract": "Abstract",
    }


def test_query_and_prompt_do_not_expose_source_identity():
    candidates = [candidate(11, 1, "Trial Alpha"), candidate(12, 2, "Trial Beta")]
    query = build_protocol_query(REVIEW)
    prompt = build_prompt(REVIEW, candidates)
    assert REVIEW["Title"] not in query
    assert REVIEW["Title"] not in prompt
    assert "Does treatment improve recovery?" in query
    assert "Corpus ID: 11" in prompt


def test_agent_tools_enforce_the_distinct_article_cap():
    class FakeRetriever:
        def __init__(self):
            self.calls = 0

        def search_text(self, query, source_ids, k):
            batches = ([11, 12, 13], [13, 14, 15])
            values = batches[self.calls]
            self.calls += 1
            return [candidate(value, rank, f"Article {value}") for rank, value in enumerate(values, 1)]

    tools = AgentCorpusTools(
        FakeRetriever(), REVIEW, k=3, max_distinct_articles=4
    )
    first = tools.search("first query")
    second = tools.search("second query")
    assert [row["corpus_id"] for row in first] == [11, 12, 13]
    assert [row["corpus_id"] for row in second] == [13, 14]
    assert tools.returned_ids == {11, 12, 13, 14}


def test_review_oracle_uses_protocol_query_and_task_labels():
    retriever = Retriever.__new__(Retriever)
    retriever.search_oracle_text = MagicMock(return_value=[])
    retriever.search_oracle(REVIEW, 3)
    query, ground_truth, source_ids, k = retriever.search_oracle_text.call_args.args
    assert "Does treatment improve recovery?" in query
    assert "Private source-review title" not in query
    assert ground_truth == [11, 12]
    assert source_ids == [10]
    assert k == 3


def test_oracle_orders_every_reference_by_retriever_score():
    import numpy as np

    class FakeModel:
        def encode(self, *args, **kwargs):
            return np.array([[1.0, 0.0]], dtype=np.float32)

    class FakeIndex:
        def reconstruct(self, position):
            vectors = {
                1: np.array([0.3, 0.0], dtype=np.float32),
                2: np.array([0.9, 0.0], dtype=np.float32),
            }
            return vectors[position]

    retriever = Retriever.__new__(Retriever)
    retriever.model = FakeModel()
    retriever.index = FakeIndex()
    retriever.index_positions = {10: 0, 11: 1, 12: 2, 13: 3}
    retriever.corpus = [candidate(value, 0, f"Article {value}") for value in range(10, 14)]
    retriever.positions = {int(row["ID"]): index for index, row in enumerate(retriever.corpus)}
    retriever._search_text = MagicMock(return_value=[candidate(13, 1, "Other")])

    oracle = retriever.search_oracle_text("protocol", [11, 12], [10], 3)
    assert [row["corpus_id"] for row in oracle] == [12, 11, 13]


def test_included_ids_are_read_from_included_section():
    candidates = [candidate(11, 1, "Trial Alpha"), candidate(12, 2, "Trial Beta")]
    report = "Corpus ID: 12 was excluded.\n\n## Included studies\n- Trial Alpha (Corpus ID: 11)"
    result = extract_included_articles(report, candidates)
    assert result["included_article_ids"] == [11]


def test_exact_long_title_is_used_when_id_is_absent():
    candidates = [
        candidate(11, 1, "Prospective evaluation of treatment recovery in adults")
    ]
    report = "## Final included studies\n- Prospective evaluation of treatment recovery in adults"
    result = extract_included_articles(report, candidates)
    assert result["included_article_ids"] == [11]
    assert result["extraction_method"] == "included_section_titles"


def test_unknown_included_id_is_not_repaired_from_title():
    candidates = [
        candidate(11, 1, "Prospective evaluation of treatment recovery in adults")
    ]
    report = "## Final included studies\n- Corpus ID: 999999 | Prospective evaluation of treatment recovery in adults"
    result = extract_included_articles(report, candidates)
    assert result["included_article_ids"] == []
    assert result["unmatched_included_article_ids"] == [999999]


def test_unknown_id_counts_in_whole_report_fallback():
    candidates = [candidate(11, 1, "Trial Alpha")]
    report = "Final evidence list\n- Corpus ID: 11\n- Corpus ID: 999999"
    result = extract_included_articles(report, candidates)
    assert result["included_article_ids"] == [11]
    assert result["unmatched_included_article_ids"] == [999999]
    assert "unmatched_included_article_count" not in result


def test_openai_client_uses_standard_arguments():
    with patch("metasyn.rag.OpenAI") as constructor:
        constructor.return_value = MagicMock()
        create_client(api_key="test-key", base_url="https://example.test/v1")
    constructor.assert_called_once_with(
        api_key="test-key", base_url="https://example.test/v1"
    )


def test_evaluator_uses_the_same_standard_openai_contract():
    from metasyn.llm_client import LLMClient

    environment = {
        "OPENAI_API_KEY": "judge-key",
        "OPENAI_BASE_URL": "https://judge.example/v1",
        "OPENAI_MODEL": "judge-model",
    }
    with patch.dict(os.environ, environment, clear=False):
        with patch("metasyn.llm_client.OpenAI") as constructor:
            LLMClient()
    constructor.assert_called_once_with(
        api_key="judge-key", base_url="https://judge.example/v1"
    )


def test_source_review_is_removed_before_top_k():
    class FakeModel:
        def encode(self, *args, **kwargs):
            import numpy as np

            return np.array([[0.0, 1.0]], dtype=np.float32)

    class FakeIndex:
        ntotal = 4

        def search(self, embedding, k):
            import numpy as np

            return (
                np.array([[1.0, 0.9, 0.8, 0.7]], dtype=np.float32),
                np.array([[0, 1, 2, 3]], dtype=np.int64),
            )

    retriever = Retriever.__new__(Retriever)
    retriever.model = FakeModel()
    retriever.index = FakeIndex()
    retriever.index_ids = [10, 11, 12, 13]
    retriever.corpus = [
        {"ID": corpus_id, "title": f"Article {corpus_id}"}
        for corpus_id in (10, 11, 12, 13)
    ]
    retriever.positions = {row["ID"]: index for index, row in enumerate(retriever.corpus)}
    results = retriever.search(REVIEW, k=2)
    assert [row["corpus_id"] for row in results] == [11, 12]
    assert retriever.fetch(11, [10])["ID"] == 11
    try:
        retriever.fetch(10, [10])
    except PermissionError:
        pass
    else:
        raise AssertionError("Source-review fetch was not rejected")


def test_id_precision_matches_the_final_evaluator():
    metrics = id_metrics([11, 12], [11, 13], [11, 12, 13])
    assert metrics["inclusion_recall"] == 0.5
    assert metrics["inclusion_precision"] == 0.5
    assert metrics["inclusion_f1"] == 0.5


def test_unmatched_included_article_ids_count_against_precision():
    metrics = id_metrics(
        [11, 12], [11], [11, 12, 13], unmatched_included_article_ids=[999999]
    )
    assert metrics["inclusion_recall"] == 0.5
    assert metrics["inclusion_precision"] == 0.5
    assert metrics["inclusion_f1"] == 0.5
    assert metrics["unmatched_included_article_count"] == 1


def test_missing_reference_criteria_are_skipped():
    from metasyn import judge as judge_module

    class FakeJudge:
        def extract_criteria(self, report):
            return ["predicted inclusion"], ["predicted exclusion"]

        def extract_conclusion_and_insights(self, report):
            return "Positive", []

        def evaluate_structure_quality(self, report):
            return 3.0, "complete enough"

    class FakeSimilarity:
        def soft_f1(self, reference, predicted):
            return 0.75

    review = {
        "inclusion_criteria": None,
        "exclusion_criteria": "Exclude reviews",
        "Effect_Direction": "Positive",
        "Key_Insights": "",
    }
    with patch.object(judge_module, "CriteriaSimilarity", return_value=FakeSimilarity()):
        metrics = judge_module.text_metrics("report", review, FakeJudge())
    assert metrics["inclusion_consistency"] is None
    assert metrics["inclusion_consistency_skipped"] is True
    assert metrics["exclusion_consistency"] == 0.75


def test_bm25_uses_the_protocol_and_excludes_the_source_review():
    from datasets import Dataset

    corpus = Dataset.from_list(
        [
            {"ID": 10, "title": "Treatment recovery source review", "abstract": "Adults"},
            {"ID": 11, "title": "Treatment recovery trial", "abstract": "Adults improved"},
            {"ID": 12, "title": "Unrelated observational report", "abstract": "Other topic"},
        ]
    )
    rows = BM25Retriever(corpus).search(REVIEW, k=2)
    assert rows[0]["corpus_id"] == 11
    assert 10 not in [row["corpus_id"] for row in rows]
