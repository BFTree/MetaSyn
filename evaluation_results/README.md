# Evaluation Results

This directory contains one metric file for each of the 1,032 public
generation results. Directory names match `generation_results`; each
`review_<ID>.json` file records `review_id`, the configuration, final metrics,
aggregate evaluator token counts, and evaluator-extracted criteria, conclusion
direction, and key insights.

`retrieval_recall` and `retrieval_precision` measure the retrieved pool.
`inclusion_recall`, `inclusion_precision`, and `inclusion_f1` measure the final
listed evidence set. `screening_accuracy` compares final include/exclude
decisions with membership in the linked reference set. The remaining metrics
are evaluator-dependent report measures described in the paper and main
README. Unmatched stated inclusions remain in the inclusion-precision
denominator.

For a reference set `G`, retrieved pool `P`, and final mapped list `L`,
`conditional_retention` is `len(P & G & L) / len(P & G)` and is null when
`P & G` is empty. `post_retrieval_loss` is `len((P & G) - L) / len(G)`. The two
are not complements because their denominators differ.
The evaluator-only `unmatched_included_article_count` field is derived from the
deduplicated unmapped ID and citation-string lists; it is not a result input.

`evaluator_token_usage` contains aggregate token counts.

| Benchmark row | Directory |
|---|---|
| RAG DeepSeek-V4-Pro / BM25 | `rag__DeepSeek-V4-Pro__bm25` |
| RAG DeepSeek-V4-Pro / BGE | `rag__DeepSeek-V4-Pro__dense_raw` |
| RAG DeepSeek-V4-Pro / MA-Retriever | `rag__DeepSeek-V4-Pro__ma_retriever` |
| RAG GLM-5.1 / BM25 | `rag__GLM-5.1__bm25` |
| RAG GLM-5.1 / BGE | `rag__GLM-5.1__dense_raw` |
| RAG GLM-5.1 / MA-Retriever | `rag__GLM-5.1__ma_retriever` |
| RAG GPT-5.4 / BM25 | `rag__gpt-5.4__bm25` |
| RAG GPT-5.4 / BGE | `rag__gpt-5.4__dense_raw` |
| RAG GPT-5.4 / MA-Retriever | `rag__gpt-5.4__ma_retriever` |
| ProtoMA GPT-5.4 / MA-Retriever | `protoma__gpt-5.4__ma_retriever` |
| GPT-Researcher / MA-Retriever | `gptresearcher__gpt-5.4__ma_retriever` |
| OpenDR / MA-Retriever | `opendeepresearch__gpt-5.4__ma_retriever` |
