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

The experiments used GPT-Researcher 0.14.7 and Open Deep Research 0.0.16. We
retained each framework's upstream planning, query generation, iterative
research, evidence integration, and final report workflow. Our wrappers supplied
the MetaSyn task prompt and runtime settings, and replaced Web retrieval with
tools over the fixed MetaSyn corpus. They did not replace the frameworks'
research or report workflows with MetaSyn-specific stages.

Both agents used the released, fine-tuned
[`BFTree/MA-Retriever`](https://huggingface.co/BFTree/MA-Retriever). They did
not use the raw `BAAI/bge-large-en-v1.5` checkpoint, which is evaluated
separately as the raw BGE retrieval baseline. Every query issued by a framework
was encoded independently by MA-Retriever.
Documents were indexed as title plus abstract, and the target source-review
record was removed before top-K truncation. No server-side publication-year
filter was applied.

The released `metasyn.agent_tools.AgentCorpusTools` is a sanitized interface
for reproducing the task-scoped local-corpus policy. It applies source-review
exclusion, returns at most 20 records per search, permits fetches only for
records previously returned in the same task, and enforces a 200-distinct-ID
exposure ceiling. `build_agent_prompt(review)` reconstructs the common task
prompt used by the runners, including the research question, PI/ECO fields,
recorded search dates, and eligibility criteria.

The formal service returned at most 20 records per call. The deduplicated union
never exceeded 82 articles in an actual-retrieval run or 62 in a GPT-Researcher
oracle run. Thus every reported agent run remained within the same 200-article
comparison budget as fixed-pool RAG without reaching that boundary. The public
adapter enforces the ceiling so new reproductions preserve this condition; the
guard would not alter any reported trace.

### GPT-Researcher wiring

GPT-Researcher was configured with its MCP retriever. Its standard
`conduct_research()` workflow issued queries and used the native MCP fast
path to select and invoke `search_metasyn_corpus`. The tool returned one MCP
observation containing up to 20 ranked records with Corpus IDs, titles, years,
abstracts, and metadata. GPT-Researcher consumed that observation through its
normal MCP-retriever research path. We then called the standard
`write_report()` workflow.

In pseudocode, the integration boundary is:

```text
config["RETRIEVER"] = "mcp"
serve search_metasyn_corpus over streamable HTTP on localhost
researcher = GPTResearcher(
    query=build_agent_prompt(review),
    report_type="deep_research",
    config_path=config_path,
    mcp_configs=[{"name": "metasyn_local",
                  "connection_url": local_mcp_url,
                  "connection_type": "streamable_http"}],
    mcp_strategy="fast",
)
await researcher.conduct_research()
    -> MCPRetriever.search_async(query)
    -> native MCP fast tool selection
    -> search_metasyn_corpus(query, k=20)
report = await researcher.write_report()
```

### Open Deep Research wiring

OpenDR was run through its official `deep_researcher` graph with
`search_api="none"`. We registered two MCP tools:

- `search_metasyn_corpus(query, k)` returns ranked Corpus IDs, titles,
  abstracts, and available metadata. The experiment service fixes the effective
  result count at 20 even when the agent requests another value of `k`.
- `fetch_metasyn_record(corpus_id, section, chunk, chunk_chars)` returns a
  bounded chunk of a record that the same task previously received from search.

The distinction from GPT-Researcher follows the frameworks' native interfaces.
OpenDR is a tool-using graph that separately chooses when to search and when to
read a retrieved record, so both search and fetch preserve its normal research
flow. The user message passed to `deep_researcher.ainvoke()` contained the
common task prompt described above; the graph's returned `final_report` was
evaluated without an additional generation stage.

A representative OpenDR tool sequence is:

```text
deep_researcher graph -> search(query_1) -> up to 20 MA-Retriever results
                      -> search(query_2) -> up to 20 MA-Retriever results
                      -> fetch(corpus_id, section, chunk) -> corpus text
                      -> upstream compression and final-report stages
```

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
