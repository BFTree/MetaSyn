<div align="center">

# MetaSyn

**Benchmarking LLM Agents on Meta-Analysis Articles from Nature Portfolio**

<p>
  <a href="https://arxiv.org/abs/2606.17041"><img alt="Paper" src="https://img.shields.io/badge/arXiv-2606.17041-B31B1B?logo=arxiv&amp;logoColor=white"></a>
  <a href="https://huggingface.co/datasets/THUIR/MetaSyn"><img alt="Dataset" src="https://img.shields.io/badge/Dataset-THUIR%2FMetaSyn-FFD21E?logo=huggingface&amp;logoColor=black"></a>
  <a href="https://huggingface.co/BFTree/MA-Retriever"><img alt="Model" src="https://img.shields.io/badge/Model-MA--Retriever-FFD21E?logo=huggingface&amp;logoColor=black"></a>
  <a href="pyproject.toml"><img alt="Python" src="https://img.shields.io/badge/Python-3.10%20%7C%203.11-3776AB?logo=python&amp;logoColor=white"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/License-MIT-2EA44F"></a>
</p>

<p>
  <a href="https://arxiv.org/abs/2606.17041">Paper</a>
  &nbsp;&middot;&nbsp;
  <a href="https://huggingface.co/datasets/THUIR/MetaSyn">Dataset</a>
  &nbsp;&middot;&nbsp;
  <a href="https://huggingface.co/BFTree/MA-Retriever">MA-Retriever</a>
  &nbsp;&middot;&nbsp;
  <a href="generation_results">Generation Results</a>
  &nbsp;&middot;&nbsp;
  <a href="evaluation_results">Evaluation Results</a>
  &nbsp;&middot;&nbsp;
  <a href="BASELINES.md">Baseline Settings</a>
</p>

</div>

## What Is a Meta-Analysis?

A meta-analysis statistically combines results from independent studies that
answer the same research question. It is usually conducted within a systematic
review, where researchers retrieve candidate studies and screen them against
predefined eligibility criteria. These criteria are often organized as PI/ECO:
Population, Intervention or Exposure, Comparison, and Outcome.

The workflow links several distinct decisions: retrieving candidate articles,
selecting evidence under the review protocol, extracting and analyzing study
results, and reporting the final synthesis. Published protocols,
included-study lists, and conclusions make retrieval, selection, and written
synthesis especially suitable for reproducible evaluation.

## MetaSyn

MetaSyn turns 422 Nature Portfolio source reviews, mainly systematic reviews
and meta-analyses, into linked benchmark tasks. Each task provides a research
question, structured PI/ECO fields, search and eligibility information, the
published included-study list, and reference synthesis labels. Stable article
IDs connect the included-study lists to one shared corpus of 140,585 PubMed
records.

The benchmark evaluates retrieval, protocol-based evidence selection, and
report synthesis. This repository provides the benchmark code, evaluator
prompts, and outputs for the 12 main configurations.

### Dataset Overview

| Statistic | Value |
|---|---:|
| Source reviews | 422 |
| Train / test reviews | 336 / 86 |
| Shared PubMed corpus | 140,585 articles |
| Review/article links | 7,374 |
| PI/ECO structure available | 100% |

The source-review split is disjoint. Included-study titles are linked to the
shared corpus by stable IDs, and the complete title lists are retained for
future matching through other literature databases.

### Benchmark at a Glance

We evaluate sparse and dense retrieval, one-pass RAG, explicit screening, and
deep-research agents. MA-Retriever reaches 91.7% Recall@200, while the highest
end-to-end inclusion recall under standard retrieval is 51.2%. Oracle and
candidate-level diagnostics show that systems still omit many reference
articles after retrieval, which makes protocol-based selection a separate and
important evaluation target.

## Repository Contents

| Path | Contents |
|---|---|
| [`src/metasyn`](src/metasyn) | Retrieval, RAG, agent adapters, and evaluation library |
| [`scripts`](scripts) | Runnable indexing, retrieval, generation, evaluation, and training commands |
| [`configs`](configs) | Settings for the reported baseline configurations |
| [`generation_results`](generation_results) | Reports and compact result records for all 12 configurations |
| [`evaluation_results`](evaluation_results) | Per-review metrics for all 12 configurations |
| [`tests`](tests) | Public interface and evaluator contract tests |

## Install

The release is validated with Python 3.11 and supports Python 3.10 and 3.11.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env
```

Set an OpenAI-compatible endpoint in `.env`:

```dotenv
OPENAI_API_KEY=
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=
```

Set `OPENAI_API_KEY` and `OPENAI_MODEL` for the endpoint you use.

Every LLM call uses the standard Python client:

```python
from openai import OpenAI

client = OpenAI(api_key=api_key, base_url=base_url)
response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
)
```

## Build the retrieval index

```bash
python scripts/build_index.py --output artifacts/ma_retriever_index
```

The command downloads the public corpus and MA-Retriever, encodes article
titles and abstracts, and builds the FAISS HNSW index used by the benchmark.

## Run retrieval

```bash
python scripts/run_retrieval.py \
  --retriever ma_retriever \
  --review-id 63 \
  --index artifacts/ma_retriever_index \
  --top-k 200 \
  --output outputs/retrieval_63.json
```

The retrieval query contains the research question and PI/ECO fields. It does
not contain the source-review title. Any corpus record corresponding to the
source review is removed before top-K truncation.

## Run one-pass RAG

```bash
python scripts/run_rag.py \
  --review-id 63 \
  --index artifacts/ma_retriever_index \
  --top-k 200 \
  --mode actual \
  --output outputs/rag_63
```

Use `--mode oracle` to place all linked included articles first. Reference
articles are ordered by their MA-Retriever score for the task query, and
ordinary candidates fill the remaining positions in their normal retrieval
order. This is a label-informed, non-deployable diagnostic that uses the
benchmark reference set. The labels affect retrieval order but are not shown
to the LLM.

To reproduce an actual-retrieval BM25 RAG row, omit `--index` and run:

```bash
python scripts/run_rag.py \
  --review-id 63 \
  --retriever bm25 \
  --top-k 200 \
  --mode actual \
  --output outputs/rag_bm25_63
```

For raw BGE, build its index with `scripts/build_index.py`, then pass
`--retriever dense_raw` and that index. The raw BGE model is selected by
default; `--retriever-model` can override it.

Each run writes `report.md` and `results.json`. The latter records the review ID,
retrieved articles, parsed final included-article list, unmatched stated citations,
model name, and API token usage when the provider returns it.

## Evaluate one report

By default, the evaluator reads `report.md` and parses its dedicated final
included-article list against the `retrieved_articles` stored in `results.json`.
Exact candidate titles and explicit `Corpus ID` values are accepted. An
unrecognized final list is an evaluation error rather than an empty prediction.
ID-based metrics do not require an API:

```bash
python scripts/evaluate.py \
  --result outputs/rag_63/results.json \
  --report outputs/rag_63/report.md \
  --output outputs/rag_63/evaluation.json \
  --id-only
```

Omit `--id-only` to also compute the evaluator-dependent criteria, direction,
insight, and structure metrics. These calls use the same OpenAI-compatible
environment variables shown above. The benchmark reports inclusion recall,
precision, F1, screening accuracy, inclusion/exclusion criteria consistency,
conclusion-direction accuracy, insight consistency, and structure quality.
Unmatched IDs stated in the final included-article list remain predicted
inclusions and therefore count against inclusion precision. The evaluator
deduplicates these entries and derives their count from the parsed list.

The same ID-only evaluation also reports four retrieval diagnostics. Let `G`
be the linked reference set, `P` the deduplicated retrieved pool, and `L` the
final mapped inclusion list:

- `retrieval_recall` is `len(P & G) / len(G)`.
- `retrieval_precision` is `len(P & G) / len(P)`.
- `conditional_retention` is `len(P & G & L) / len(P & G)`.
- `post_retrieval_loss` is `len((P & G) - L) / len(G)`.

Conditional retention is `null` when no reference article was retrieved. It is
not the complement of post-retrieval loss because the two metrics use different
denominators. The nine main pipeline metrics are unchanged; these four values
make retrieval and downstream loss directly reproducible from the same result.

### Strict JSON alternative

Systems that already resolve their own final citations can bypass report-list
parsing with `--selection-source json`. Their `results.json` must use this exact
schema:

```json
{
  "review_id": 63,
  "retrieved_article_ids": [101, 102, 103],
  "included_article_ids": [101, 103],
  "unmatched_included_article_ids": [],
  "unmatched_included_entries": []
}
```

`included_article_ids` must be a subset of `retrieved_article_ids`. Put an
explicit but unmapped numeric ID in `unmatched_included_article_ids`, and put an
unmapped title or other citation string in `unmatched_included_entries`. Do not
supply `unmatched_included_article_count`; that field is rejected as input.
The evaluator deduplicates both lists, derives the precision denominator, and
reports `unmatched_included_article_count` as the derived number of unique
unmapped IDs and citation strings. A full evaluator-dependent run still
needs `report.md` for the criteria and synthesis metrics:

```bash
python scripts/evaluate.py \
  --result outputs/my_system/review_63/results.json \
  --report outputs/my_system/review_63/report.md \
  --selection-source json \
  --judge-model gpt-5.5 \
  --output outputs/my_system/review_63/evaluation.json
```

Each evaluation records its UTC timestamp, evaluator and prompt versions,
dataset ID and revision, judge model, report hash, and API token usage. Exhausted
API retries or invalid judge responses produce `status: failed` and null text
metrics. They are never converted into low system scores.

## Evaluate the complete test set

Place exactly one `results.json` and, unless using `--id-only` with strict JSON,
one `report.md` under a directory for each of the 86 test reviews:

```text
outputs/my_system/
  review_23/results.json
  review_23/report.md
  ...
  review_466/results.json
  review_466/report.md
```

Then run:

```bash
python scripts/evaluate_all.py \
  --results-dir outputs/my_system \
  --selection-source report \
  --judge-model gpt-5.5 \
  --output outputs/my_system/evaluation.json
```

The command checks that every released test review appears exactly once before
making evaluator calls. It writes all per-review records, macro averages, and
the valid denominator for each metric. Any missing review or failed evaluator
call makes the run fail and suppresses the aggregate score.

## Train MA-Retriever

```bash
python scripts/train_retriever.py \
  --base-model BAAI/bge-large-en-v1.5 \
  --output artifacts/ma_retriever
```

The training script uses only training-review links and removes every article
linked to a test review from the positive training pairs. The released model
was trained for one epoch with Multiple Negatives Ranking Loss.

## Using other agents

`AgentCorpusTools` provides the task-scoped search and fetch interface used by
the agent experiments. It excludes source-review records from every search and
allows an article to be fetched only after that task has returned it:

```python
from metasyn.agent_tools import AgentCorpusTools, build_agent_prompt

tools = AgentCorpusTools(retriever, review, k=20, max_distinct_articles=200)
search_results = tools.search("focused protocol query")
article = tools.fetch(search_results[0]["corpus_id"])
prompt = build_agent_prompt(review)
```

This interface can be connected to GPT-Researcher, Open Deep Research, or
another agent without copying those third-party projects into this repository.
The experiments used GPT-Researcher 0.14.7 and Open Deep Research 0.0.16.
Evaluate the explicit final article list with the same result schema.

See [BASELINES.md](BASELINES.md) and `configs/final_experiments.json` for the
exact BM25, raw-BGE, ProtoMA, GPT-Researcher, and OpenDR settings.

## Released baseline outputs

[`generation_results`](generation_results/README.md) contains the original
generated reports plus compact per-review result records for the nine one-pass
RAG configurations, ProtoMA, GPT-Researcher, and OpenDR. All 12 configurations
cover the same 86 test reviews, for 1,032 report/result pairs.
The compact records omit full retrieved-article objects, so reevaluate them with
`--selection-source json`. Newly generated `run_rag.py` outputs also support
report-based list parsing.

[`evaluation_results`](evaluation_results/README.md) contains the corresponding
1,032 per-review metric records and evaluator-extracted criteria, conclusion
directions, and key insights. The generated reports are included unchanged.

## Data and licensing

Code and project-authored annotations are MIT licensed. PubMed metadata,
abstracts, article identifiers, source-review excerpts, and PMC-derived text
retain their upstream terms; the MIT license does not relicense third-party
content. See the dataset card for field-level details.

## Citation

```bibtex
@misc{metasyn2026,
  title         = {Benchmarking {LLM} Agents on Meta-Analysis Articles from {Nature} Portfolio},
  author        = {Anzhe Xie and Weihang Su and Yujia Zhou and Yiqun Liu and Min Zhang and Qingyao Ai},
  year          = {2026},
  eprint        = {2606.17041},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2606.17041}
}
```
