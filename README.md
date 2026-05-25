# Benchmarking LLM Agents on Meta-Analysis Articles from Nature Portfolio



[![Dataset](https://img.shields.io/badge/🤗%20dataset-MetaSyn-blue)](https://huggingface.co/datasets/BFTree/MetaSyn)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](.)

## What is a Meta-Analysis?

A **meta-analysis** is the gold standard of evidence synthesis in biomedical and social science research. It systematically identifies *all* published studies on a clinical question, screens them against explicit eligibility criteria (usually framed as PICO: **P**opulation, **I**ntervention, **C**omparator, **O**utcome), extracts quantitative effect sizes, and pools them into a single estimate with formal uncertainty quantification.

What makes meta-analysis unusually demanding and unusually useful as a benchmark substrate is that every intermediate decision is **auditable**: the search query is recorded, each inclusion/exclusion decision is justified against stated criteria, and the final statistical estimate is fully reproducible. This means ground truth can be verified at every stage of the pipeline, not just at the final output.

## MetaSyn

MetaSyn is a dataset of **442 meta-analyses** drawn from the *Nature* Portfolio (2015–2024) and curated to benchmark LLM agent pipelines on the complete meta-analysis workflow. Each entry pairs a published meta-analysis with:

- A **retrieval corpus** of 140,585 PubMed-indexed articles spanning all included topics
- Expert-annotated **PICO/ECO criteria** and **search strategies**
- A **hard-negative set** of articles that share the topic but fail at least one eligibility criterion
- Ground-truth **effect size, heterogeneity, and conclusion** fields

The core challenge is end-to-end: given only a research question and eligibility criteria, a system must retrieve, screen, extract, and synthesize — replicating the full pipeline that took human experts weeks.

### Dataset Statistics

| | Meta-analyses | Corpus articles |
|--|:--:|:--:|
| Train | 354 | ~112k |
| Test | 88 | ~28k |
| **Total** | **442** | **140,585** |

| | Value |
|--|:--:|
| Median included studies per MA | 14 |
| Mean included studies per MA | 18.3 |
| Retrieval ceiling @ K=200 | 90.9% |

### Key Findings

No system we evaluated recovers more than **52.7%** of ground-truth included literature end-to-end, despite a retrieval ceiling of 90.9% at K=200. The bottleneck is screening: current LLMs fail to reliably distinguish ground-truth studies from hard negatives in pools of comparable topical relevance.

| Configuration | Inclusion Recall |
|--|:--:|
| Best RAG pipeline (K=200) | 52.7% |
| Retrieval ceiling (K=200) | 90.9% |

---

## Repository Structure

```
MetaSyn/
├── data/
│   └── README.md          ← Dataset fields, construction, and download
└── evaluation/
    ├── README.md          ← Evaluation protocol and metrics
    ├── framework/         ← Evaluator implementation
    │   ├── evaluator.py
    │   ├── llm_client.py
    │   └── semantic_similarity.py
    └── scripts/
        └── run_evaluation.py
```

## Quick Start

### 1. Install

```bash
pip install -r requirements.txt
```

### 2. Download the dataset

```
data/
├── papers.json      # 442 meta-analysis records with annotations
├── corpus.json      # 140,585 PubMed articles
└── test_ids.json    # 88 test-split paper IDs
```

Available at [HuggingFace — BFTree/MetaSyn](https://huggingface.co/datasets/BFTree/MetaSyn).

### 3. Configure the LLM judge

```bash
cp .env.example .env
# Set OPENAI_API_KEY and OPENAI_BASE_URL
```

### 4. Evaluate your system

Place your system outputs under `results/<system_name>/`:

```
results/
└── my_system/
    └── paper_63.json   # one file per test paper
```

Then run:

```bash
python evaluation/scripts/run_evaluation.py \
    --corpus data/corpus.json \
    --papers data/papers.json \
    --test-ids data/test_ids.json \
    --results-dir results/my_system/ \
    --output-dir evaluation/results/
```

See [evaluation/README.md](evaluation/README.md) for output format and metric definitions.

## Citation

```bibtex
@article{metasyn2026,
  title   = {Benchmarking {LLM} Agents on Meta-Analysis Articles from {Nature} Portfolio},
  author  = {Anzhe Xie and Weihang Su and Yujia Zhou and Yiqun Liu and Qingyao Ai},
  year    = {2026},
}
```

## License

Code: [MIT](LICENSE). Dataset: subject to Nature Portfolio terms of use.
