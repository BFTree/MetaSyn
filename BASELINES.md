# Baseline Reproduction

The exact final settings are in `configs/final_experiments.json`. All systems
use the public review split and corpus, exclude `source_review_corpus_ids`
before top-K truncation, and do not apply a coarse publication-year filter.

## Retrieval and one-pass RAG

`scripts/run_retrieval.py` supports the BM25, raw BGE, and MA-Retriever
settings. Build separate dense indexes with `scripts/build_index.py` and pass
either `BAAI/bge-large-en-v1.5` or `BFTree/MA-Retriever`. The fixed-pool RAG
prompt and included-article parser in `metasyn.rag` are the final experiment
versions.

For one-pass RAG, `scripts/run_rag.py --retriever bm25` runs the sparse
configuration without an index. Use `--retriever dense_raw` with the raw BGE
index, or the default `--retriever ma_retriever` with the released
MA-Retriever index.

## GPT-Researcher and Open Deep Research

The experiments used GPT-Researcher 0.14.7 and Open Deep Research 0.0.16.
`metasyn.agent_tools.AgentCorpusTools` is the thin local-corpus adapter: expose
its `search` and `fetch` methods through the framework's tool interface and use
`build_agent_prompt(review)` as the task prompt. Search is fixed at 20 records,
at most 200 distinct article IDs are exposed across calls, fetch is limited to
records previously returned in that task, and oracle mode
scores every linked reference for each adaptive query before filling remaining
positions from normal retrieval.

Oracle mode is a label-informed, non-deployable diagnostic. It uses each
review's benchmark reference set to change the retrieval order, but it does not
show those labels to the LLM.

GPT-Researcher uses two iterations, a 1,200-word target, 4,000 abstract
characters per search result, 6,000 characters per fetch, and 120,000-character
research and report contexts. OpenDR uses two concurrent research units, two
researcher iterations, at most ten ReAct tool calls, ten searches, and 100
fetches. Its search and fetch limits are 2,500 and 3,000 characters. Its
summarization, research, compression, and final-report output caps are 3,000,
4,000, 3,000, and 5,000 tokens. These are caps; each run records the calls it
actually makes.

## ProtoMA

ProtoMA remains an upstream workflow rather than copied third-party source.
The final run generates 3-5 PI/ECO queries, merges and deduplicates MA-Retriever
results to 200 candidates, screens batches of 25 using 500 abstract characters,
and passes up to 3,000 title-and-abstract characters per selected article into
its extraction stages. It uses no benchmark inclusion/exclusion annotations;
the exact remaining limits are in the public configuration file.

All model calls made by local wrappers should use `OPENAI_API_KEY`,
`OPENAI_BASE_URL`, and `OPENAI_MODEL` with the standard OpenAI client pattern
shown in the main README.
