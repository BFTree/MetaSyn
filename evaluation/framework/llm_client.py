"""
LLM Client for evaluation tasks.

Handles all LLM-based extractions and evaluations.
"""

import json
import os
import re
from typing import Dict, List, Optional, Tuple
from openai import OpenAI


class LLMClient:
    """
    LLM client for evaluation tasks.

    Configuration from environment variables:
        - OPENAI_API_KEY: API key (required)
        - OPENAI_MODEL: Model name (default: gpt-5.4)
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        max_retries: int = 3
    ):
        self.model = model or os.environ.get("OPENAI_MODEL", "gpt-5.4")
        self.max_retries = max_retries
        self.client = OpenAI(api_key=api_key or os.environ.get("OPENAI_API_KEY"))

    def _call(self, prompt: str, json_response: bool = True) -> str:
        """
        Call LLM API.

        Args:
            prompt: User prompt
            json_response: Whether to request JSON response

        Returns:
            Response text
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert evaluator of systematic reviews and meta-analyses. Extract information precisely and return valid JSON when requested."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            response_format={"type": "json_object"} if json_response else None,
        )
        return response.choices[0].message.content

    def _parse_json(self, response: str) -> Optional[Dict]:
        """Parse JSON from LLM response with retry support."""
        # Try to find JSON object in response
        match = re.search(r'\{.*\}', response, re.DOTALL)
        json_str = match.group() if match else response

        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            print(f"  JSON parse error: {e}")
            print(f"  Response: {response[:200]}...")
            return None

    def _call_with_retry(self, prompt: str, json_response: bool = True) -> Optional[Dict]:
        """Call LLM and parse JSON with retry support."""
        for attempt in range(self.max_retries):
            try:
                response = self._call(prompt, json_response)
                result = self._parse_json(response)
                if result is not None:
                    return result
                print(f"  Retry {attempt + 1}/{self.max_retries}...")
            except Exception as e:
                print(f"  Attempt {attempt + 1} failed: {e}")
                if attempt < self.max_retries - 1:
                    print(f"  Retry {attempt + 1}/{self.max_retries}...")
        return None

    def extract_criteria(self, report_text: str) -> Tuple[Optional[List[str]], Optional[List[str]]]:
        """
        Extract inclusion and exclusion criteria from meta-analysis report.

        Args:
            report_text: Full report text

        Returns:
            (inclusion_criteria, exclusion_criteria)
            Returns empty list [] if not found (not null)
        """
        prompt = f"""Background: This is a systematic review/meta-analysis report. Extract the inclusion and exclusion criteria.

Requirements:
1. Extract criteria verbatim from the report - do not paraphrase or summarize
2. Each criterion should be a complete sentence or phrase exactly as written
3. Look for sections describing study selection, eligibility, inclusion, or exclusion criteria
4. If criteria are found, return them as a list of strings
5. If no criteria are found, return an empty list []
6. Return ONLY valid JSON - no markdown, no explanations

JSON Format:
{{
    "inclusion_criteria": ["criterion 1", "criterion 2", ...],
    "exclusion_criteria": ["criterion 1", "criterion 2", ...]
}}

Example output if found:
{{
    "inclusion_criteria": ["Randomized controlled trials", "Studies published in English"],
    "exclusion_criteria": ["Animal studies", "Case reports"]
}}

Example output if not found:
{{
    "inclusion_criteria": [],
    "exclusion_criteria": []
}}

Report text:
---
{report_text}
---

Extract criteria now:
"""
        result = self._call_with_retry(prompt, json_response=True)

        if result is None:
            print("  Warning: Could not extract criteria, returning empty lists")
            return [], []

        inclusion = result.get("inclusion_criteria")
        exclusion = result.get("exclusion_criteria")

        # Convert null/None to empty lists
        if inclusion is None:
            inclusion = []
        if exclusion is None:
            exclusion = []

        return (inclusion, exclusion)

    def extract_conclusion_and_insights(self, report_text: str) -> Tuple[Optional[str], Optional[List[str]]]:
        """
        Extract conclusion direction and key insights from report.

        IMPORTANT: Extract exact quotes for insights, do not paraphrase.

        Args:
            report_text: Full report text

        Returns:
            (conclusion_direction, key_insights)
            where conclusion_direction is "Positive", "Negative", or "Mixed"
            Returns empty list [] for insights if not found (not null)
        """
        prompt = f"""Background: This is a systematic review/meta-analysis report. Extract the main conclusion direction and key insights.

Requirements:
1. Conclusion direction must be exactly one of: "Positive", "Negative", or "Mixed"
   - "Positive": The intervention/treatment shows beneficial effects
   - "Negative": The intervention/treatment shows harmful effects or no benefit
   - "Mixed": Results are inconclusive, conflicting, or unclear
2. Key insights must be EXACT word-for-word quotes from the report - do NOT paraphrase
3. Each insight should be a complete sentence or phrase as written in the report
4. Look for sections titled "Conclusion", "Discussion", "Key Findings", "Results", "Summary"
5. If insights are found, return them as a list of strings
6. If no insights are found, return an empty list []
7. Return ONLY valid JSON - no markdown, no explanations

JSON Format:
{{
    "conclusion_direction": "Positive",
    "key_insights": ["exact quote 1", "exact quote 2", ...]
}}

Example output:
{{
    "conclusion_direction": "Positive",
    "key_insights": ["The intervention significantly improved outcomes compared to control", "Subgroup analysis showed consistent benefits across populations"]
}}

Report text:
---
{report_text}
---

Extract conclusion and insights now:
"""
        result = self._call_with_retry(prompt, json_response=True)

        if result is None:
            print("  Warning: Could not extract conclusion/insights, returning None")
            return None, []

        direction = result.get("conclusion_direction")
        insights = result.get("key_insights")

        # Convert null/None insights to empty list
        if insights is None:
            insights = []

        return (direction, insights)

    def evaluate_insights_consistency(
        self,
        extracted_insights: List[str],
        ground_truth_insights: str
    ) -> float:
        """
        Evaluate consistency between extracted and ground truth insights.

        Args:
            extracted_insights: Insights extracted from report
            ground_truth_insights: Ground truth insights (may be multi-line)

        Returns:
            Consistency score (0-1)
            Returns 0.0 if extracted_insights is empty
        """
        # Parse GT insights into individual items
        gt_items = [s.strip() for s in ground_truth_insights.split('\n') if s.strip() and len(s) > 20]

        if not gt_items:
            print("  Warning: No ground truth insights to compare, returning 0.5")
            return 0.5

        if not extracted_insights:
            print("  Warning: No extracted insights to compare, returning 0.0")
            return 0.0

        gt_text = "\n".join(gt_items)
        extracted_text = "\n".join(extracted_insights)

        prompt = f"""Task: Evaluate how well the extracted key insights from a systematic review/meta-analysis report match the ground truth key insights.

Score the coverage on a scale of 0.0 to 1.0.

Scoring Guidelines:
- 1.0 = Perfect coverage: All ground truth insights are covered by extracted insights
- 0.8 = Good coverage: Most ground truth insights (75%+) are covered
- 0.6 = Fair coverage: Some ground truth insights (50-74%) are covered
- 0.4 = Poor coverage: Few ground truth insights (25-49%) are covered
- 0.2 = Very poor coverage: Very few ground truth insights (<25%) are covered
- 0.0 = No coverage: Extracted insights are completely different, irrelevant, or empty

Consider semantic similarity, not just exact word matching. An extracted insight "covers" a ground truth insight if they convey the same finding or conclusion.

Ground Truth Insights:
---
{gt_text}
---

Extracted Insights:
---
{extracted_text}
---

JSON Format:
{{
    "consistency_score": 0.8,
    "reason": "One sentence explaining the score based on coverage"
}}

Evaluate now:
"""
        result = self._call_with_retry(prompt, json_response=True)

        if result is None:
            print("  Warning: Could not evaluate insights, returning 0.0")
            return 0.0

        score = result.get("consistency_score")
        if score is None:
            print("  Warning: No consistency_score in response, returning 0.0")
            return 0.0

        try:
            return float(score)
        except (ValueError, TypeError):
            print(f"  Warning: Invalid score value: {score}, returning 0.0")
            return 0.0

    def evaluate_structure_quality(self, report_text: str) -> Tuple[float, str]:
        """
        Evaluate report structure quality.

        Args:
            report_text: Full report text

        Returns:
            (score, reason) where score is 1-5
            Returns (1.0, "Could not evaluate") on error
        """
        prompt = f"""Background: This is a systematic review/meta-analysis report. Evaluate its structure and organization quality.

Task: Rate the structure quality on a scale of 1 to 5.

Scoring Guidelines:
1 = Poor: Missing most required sections (abstract, introduction, methods, results, discussion, conclusion, references); disorganized
2 = Fair: Some sections present but major gaps; unclear organization or flow
3 = Good: Most required sections present (Abstract, Introduction, Methods, Results, Discussion/Conclusion, References)
4 = Very Good: Complete structure, well-organized, includes meta-analysis elements (search strategy, screening process, data synthesis method)
5 = Excellent: Comprehensive structure with excellent organization and all PRISMA-style rigor elements (detailed search strategy, inclusion/exclusion criteria, quality assessment, synthesis methods)

Consider:
- Are all required sections present? (Abstract, Introduction, Methods, Results, Discussion, Conclusion, References)
- Is the logical flow clear and easy to follow?
- Are meta-analysis-specific elements included? (search strategy, screening criteria, data extraction method, synthesis approach)

Report text:
---
{report_text}
---

JSON Format:
{{
    "score": 4,
    "reason": "One sentence explaining the score with specific observations"
}}

Evaluate now:
"""
        result = self._call_with_retry(prompt, json_response=True)

        if result is None:
            print("  Warning: Could not evaluate structure, returning score 1.0")
            return (1.0, "Could not evaluate - parse error")

        score = result.get("score")
        reason = result.get("reason", "")

        # Default score if null/invalid
        if score is None:
            print("  Warning: No score in response, returning 1.0")
            return (1.0, "Could not evaluate - no score")

        try:
            score_float = float(score)
            if score_float < 1 or score_float > 5:
                print(f"  Warning: Score {score_float} out of range, clamping to 1-5")
                score_float = max(1, min(5, score_float))
            return (score_float, reason)
        except (ValueError, TypeError):
            print(f"  Warning: Invalid score value: {score}, returning 1.0")
            return (1.0, "Could not evaluate - invalid score")
