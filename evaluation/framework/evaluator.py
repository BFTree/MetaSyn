"""
Report Evaluator - Main evaluation orchestration

Evaluates a generated meta-analysis report against ground truth.

Interface:
    evaluate(
        report_text: str,           # Full report text
        included_ids: List[int],    # Included paper IDs
        retrieved_ids: List[int]    # Retrieved paper IDs
    ) -> Dict
"""

import json
from typing import Dict, List, Optional, Set

# Support both package import and direct script import
try:
    from .llm_client import LLMClient
    from .semantic_similarity import SemanticSimilarity
except ImportError:
    from llm_client import LLMClient
    from semantic_similarity import SemanticSimilarity


class ReportEvaluator:
    """
    Evaluates a generated meta-analysis report.

    10 Metrics:
    1-3. retrieval_recall, retrieval_precision, retrieval_f1
    4-5. screening_accuracy, screening_f1
    6-7. inclusion_consistency, exclusion_consistency (soft F1)
    8.   conclusion_direction_accuracy
    9.   insights_consistency (LLM evaluated)
    10.  structure_quality (LLM evaluated, 1-5)
    """

    def __init__(
        self,
        corpus_path: str,
        papers_path: str,
        model: Optional[str] = None
    ):
        """
        Initialize evaluator.

        Args:
            corpus_path: Path to corpus.json (not loaded - kept for reference)
            papers_path: Path to papers.json (ground truth)
            model: LLM model name (optional, overrides OPENAI_MODEL env)
        """
        # Don't load corpus - it's 3.3GB and not needed for evaluation
        # All metrics use papers.json (ground truth) and passed IDs
        self.corpus_path = corpus_path  # Kept for potential future use
        self.papers = self._load_json(papers_path)
        self.papers_by_id = {item["ID"]: item for item in self.papers}

        self.llm = LLMClient(model=model)

    def _load_json(self, path: str) -> List[dict]:
        """Load JSON file."""
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def evaluate(
        self,
        report_text: str,
        included_ids: List[int],
        retrieved_ids: List[int],
        ground_truth_paper_id: int
    ) -> Dict:
        """
        Evaluate a single report.

        Args:
            report_text: Full report markdown text
            included_ids: Paper IDs included in the report
            retrieved_ids: Paper IDs that were retrieved
            ground_truth_paper_id: ID of the ground truth paper in papers.json

        Returns:
            Dictionary with metrics and extracted data:
            {
                "metrics": {...},
                "extracted_data": {...}
            }
        """
        # Get ground truth
        ground_truth = self.papers_by_id.get(ground_truth_paper_id)
        if not ground_truth:
            return {"error": f"Ground truth paper {ground_truth_paper_id} not found"}

        ground_truth_ids = set(ground_truth.get("matched_corpus_ids", []))
        included_set = set(included_ids)
        retrieved_set = set(retrieved_ids)

        result = {
            "ground_truth_paper_id": ground_truth_paper_id,
            "metrics": {},
            "extracted_data": {}
        }

        # ========== LLM Extractions (Calls 1-3) ==========

        # Call 1: Extract criteria
        inclusion_criteria, exclusion_criteria = self.llm.extract_criteria(report_text)
        result["extracted_data"]["inclusion_criteria"] = inclusion_criteria
        result["extracted_data"]["exclusion_criteria"] = exclusion_criteria

        # Call 2-3: Extract conclusion direction and key insights
        conclusion_direction, key_insights = self.llm.extract_conclusion_and_insights(report_text)
        result["extracted_data"]["conclusion_direction"] = conclusion_direction
        result["extracted_data"]["key_insights"] = key_insights

        # ========== Metrics 1-3: Retrieval ==========

        if not ground_truth_ids:
            # No GT - skip retrieval metrics
            result["metrics"]["retrieval_recall"] = None
            result["metrics"]["retrieval_precision"] = None
            result["metrics"]["retrieval_f1"] = None
        elif not included_set:
            # No papers included - all zeros
            result["metrics"]["retrieval_recall"] = 0.0
            result["metrics"]["retrieval_precision"] = 0.0
            result["metrics"]["retrieval_f1"] = 0.0
        else:
            tp = len(included_set & ground_truth_ids)
            recall = tp / len(ground_truth_ids)
            precision = tp / len(included_set) if included_set else 0
            f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

            result["metrics"]["retrieval_recall"] = round(recall, 4)
            result["metrics"]["retrieval_precision"] = round(precision, 4)
            result["metrics"]["retrieval_f1"] = round(f1, 4)

        # ========== Metric 4: Screening Accuracy ==========

        if not retrieved_set:
            # No papers retrieved - score 0
            result["metrics"]["screening_accuracy"] = 0.0
            result["metrics"]["screening_f1"] = 0.0
        else:
            correct = sum(
                1 for pid in retrieved_set
                if (pid in included_set) == (pid in ground_truth_ids)
            )
            result["metrics"]["screening_accuracy"] = round(correct / len(retrieved_set), 4)

            # Screening F1: treat screening as binary classification
            # True Positives: correctly included (in included_set AND in ground_truth)
            # False Positives: incorrectly included (in included_set BUT NOT in ground_truth)
            # False Negatives: incorrectly excluded (NOT in included_set BUT in ground_truth)
            tp_screening = len(included_set & ground_truth_ids)
            fp_screening = len(included_set - ground_truth_ids)
            fn_screening = len(ground_truth_ids - included_set)

            precision_screening = tp_screening / (tp_screening + fp_screening) if (tp_screening + fp_screening) > 0 else 0
            recall_screening = tp_screening / (tp_screening + fn_screening) if (tp_screening + fn_screening) > 0 else 0

            if precision_screening + recall_screening > 0:
                result["metrics"]["screening_f1"] = round(2 * precision_screening * recall_screening / (precision_screening + recall_screening), 4)
            else:
                result["metrics"]["screening_f1"] = 0.0

        # ========== Metrics 5-6: Criteria Consistency (Semantic) ==========

        gt_inclusion = ground_truth.get("inclusion_criteria")
        gt_exclusion = ground_truth.get("exclusion_criteria")

        # Inclusion consistency
        if gt_inclusion is None:
            result["metrics"]["inclusion_consistency"] = None
            result["metrics"]["inclusion_consistency_skipped"] = True
        else:
            gt_inc_items = [s.strip() for s in gt_inclusion.split(';') if s.strip()]
            if not gt_inc_items:
                result["metrics"]["inclusion_consistency"] = 0.0
                result["metrics"]["inclusion_consistency_skipped"] = False
            elif not inclusion_criteria:
                # Extraction failed - score 0
                result["metrics"]["inclusion_consistency"] = 0.0
                result["metrics"]["inclusion_consistency_skipped"] = False
            else:
                sim_result = SemanticSimilarity.compute_soft_recall_precision_f1(
                    gt_inc_items,
                    inclusion_criteria
                )
                result["metrics"]["inclusion_consistency"] = sim_result.get("soft_f1")
                result["metrics"]["inclusion_consistency_skipped"] = False

        # Exclusion consistency
        if gt_exclusion is None:
            result["metrics"]["exclusion_consistency"] = None
            result["metrics"]["exclusion_consistency_skipped"] = True
        else:
            gt_exc_items = [s.strip() for s in gt_exclusion.split(';') if s.strip()]
            if not gt_exc_items:
                result["metrics"]["exclusion_consistency"] = 0.0
                result["metrics"]["exclusion_consistency_skipped"] = False
            elif not exclusion_criteria:
                # Extraction failed - score 0
                result["metrics"]["exclusion_consistency"] = 0.0
                result["metrics"]["exclusion_consistency_skipped"] = False
            else:
                sim_result = SemanticSimilarity.compute_soft_recall_precision_f1(
                    gt_exc_items,
                    exclusion_criteria
                )
                result["metrics"]["exclusion_consistency"] = sim_result.get("soft_f1")
                result["metrics"]["exclusion_consistency_skipped"] = False

        # ========== Metric 7: Conclusion Direction Accuracy ==========

        gt_direction = ground_truth.get("Effect_Direction")
        if gt_direction is None or gt_direction == "NR":
            result["metrics"]["conclusion_direction_accuracy"] = None
            result["metrics"]["conclusion_direction_skipped"] = True
        elif conclusion_direction is None:
            # Extraction failed - score 0
            result["metrics"]["conclusion_direction_accuracy"] = 0.0
            result["metrics"]["conclusion_direction_skipped"] = False
        else:
            match = 1 if conclusion_direction == gt_direction else 0
            result["metrics"]["conclusion_direction_accuracy"] = match
            result["metrics"]["conclusion_direction_skipped"] = False

        # ========== Metric 8: Insights Consistency (LLM) ==========
        # Call 4

        gt_insights = ground_truth.get("Key_Insights", "")
        if not gt_insights:
            result["metrics"]["insights_consistency"] = None
            result["metrics"]["insights_consistency_skipped"] = True
        elif not key_insights:
            # Extraction failed - score 0
            result["metrics"]["insights_consistency"] = 0.0
            result["metrics"]["insights_consistency_skipped"] = False
        else:
            consistency = self.llm.evaluate_insights_consistency(
                key_insights,
                gt_insights
            )
            result["metrics"]["insights_consistency"] = round(consistency, 4) if consistency else 0.0
            result["metrics"]["insights_consistency_skipped"] = False

        # ========== Metric 9: Structure Quality (LLM) ==========
        # Call 5

        structure_score, structure_reason = self.llm.evaluate_structure_quality(report_text)
        result["metrics"]["structure_quality"] = round(structure_score, 2)
        result["metrics"]["structure_quality_reason"] = structure_reason

        return result

    def evaluate_from_files(
        self,
        report_text: str,
        results_json_path: str
    ) -> Dict:
        """
        Evaluate from report text and results.json.

        Args:
            report_text: Full report text
            results_json_path: Path to results.json

        Returns:
            Evaluation result dictionary
        """
        with open(results_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        paper_id = data.get("paper_id")
        included_ids = data.get("included_paper_ids", [])
        retrieved_ids = [p.get("corpus_id") for p in data.get("retrieved_papers", []) if "corpus_id" in p]

        return self.evaluate(
            report_text=report_text,
            included_ids=included_ids,
            retrieved_ids=retrieved_ids,
            ground_truth_paper_id=paper_id
        )
