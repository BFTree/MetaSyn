"""
Evaluation Framework for Automated Meta-Analysis Generation

This framework evaluates generated meta-analysis reports against ground truth.

Components:
    - evaluator: ReportEvaluator class for evaluating single reports
    - llm_client: LLMClient class for LLM-based extractions and evaluations
    - semantic_similarity: SemanticSimilarity class for semantic similarity computation

Usage:
    from evaluator import ReportEvaluator

    evaluator = ReportEvaluator(corpus_path, papers_path, llm_api_key, llm_api_base)
    result = evaluator.evaluate(report_text, included_ids, retrieved_ids, ground_truth_paper_id)

See EVALUATION_DESIGN.md for detailed design documentation.
"""

__version__ = "1.0.0"
__all__ = ["ReportEvaluator", "LLMClient", "SemanticSimilarity"]
