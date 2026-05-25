# Evaluation Framework

MetaSyn provides a reference evaluator for assessing system outputs against the ground truth in `papers.json`. Evaluation covers the full pipeline in 9 metrics across retrieval, screening, criteria extraction, and synthesis quality.

---

## Metrics

| # | Metric | What it measures | Method |
|---|--------|-----------------|--------|
| 1 | `retrieval_recall` | Fraction of ground-truth included studies retrieved | Set intersection |
| 2 | `retrieval_precision` | Fraction of retrieved studies that are ground-truth | Set intersection |
| 3 | `retrieval_f1` | Harmonic mean of recall and precision | Set intersection |
| 4 | `screening_accuracy` | Decision accuracy over the retrieved pool | Set intersection |
| 5 | `inclusion_consistency` | Soft-F1 between extracted and GT inclusion criteria | Semantic similarity |
| 6 | `exclusion_consistency` | Soft-F1 between extracted and GT exclusion criteria | Semantic similarity |
| 7 | `conclusion_direction_accuracy` | Match against GT `Effect_Direction` | LLM extraction |
| 8 | `insights_consistency` | Coverage of GT key findings | LLM judge (0–1) |
| 9 | `structure_quality` | Report completeness and organisation | LLM judge (1–5) |

Metrics 1–6 require no LLM calls. Metrics 7–9 use approximately 5 LLM calls per report.

---

## Input Format

Place one JSON file per test paper under your results directory:

```
results/my_system/
├── paper_63.json
├── paper_24.json
└── ...
```

Each file must contain:

```json
{
  "paper_id": 63,
  "report": "Full text of the generated meta-analysis report...",
  "retrieved_ids": [1234, 5678, ...],
  "included_ids": [1234, ...]
}
```

| Field | Description |
|-------|-------------|
| `paper_id` | Integer ID matching `papers.json` |
| `report` | Full text of the generated report (used for metrics 5–9) |
| `retrieved_ids` | Corpus IDs your system retrieved before screening |
| `included_ids` | Corpus IDs your system decided to include after screening |

---

## Running the Evaluator

```bash
# Set up LLM judge credentials
cp .env.example .env
# Edit .env: set OPENAI_API_KEY and OPENAI_BASE_URL

# Run evaluation
python evaluation/scripts/run_evaluation.py \
    --corpus data/corpus.json \
    --papers data/papers.json \
    --test-ids data/test_ids.json \
    --results-dir results/my_system/ \
    --output-dir evaluation/results/
```

### Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | — | API key (required for metrics 7–9) |
| `OPENAI_MODEL` | `gpt-5.4` | Judge model |

---

## Output Format

One JSON file per system:

```json
{
  "system": "my_system",
  "evaluated_at": "2026-05-25T12:00:00",
  "num_papers": 88,
  "aggregated": {
    "retrieval_recall":              0.527,
    "retrieval_recall_std":          0.18,
    "screening_accuracy":            0.71,
    "inclusion_consistency":         0.63,
    "exclusion_consistency":         0.58,
    "conclusion_direction_accuracy": 0.74,
    "insights_consistency":          0.61,
    "structure_quality":             3.8
  },
  "per_paper": [
    {
      "paper_id": 63,
      "metrics": { "retrieval_recall": 0.71, "..." : "..." }
    }
  ]
}
```

---

## Framework Internals

| File | Role |
|------|------|
| `framework/evaluator.py` | Main `ReportEvaluator` class; orchestrates all 9 metrics |
| `framework/llm_client.py` | OpenAI-compatible LLM client for extraction and judging |
| `framework/semantic_similarity.py` | Soft-F1 via `sentence-transformers` (metrics 5–6) |
| `scripts/run_evaluation.py` | CLI entry point; scans results dir and writes output JSON |
