# Generation Results

This directory contains the standard-retrieval outputs behind the main
end-to-end table: 12 configurations evaluated on all 86 test reviews, for
1,032 review-configuration pairs.

Each configuration uses the directory name `system__model__retriever`. Each
`review_<ID>` directory contains:

- `report.md`: the original generated report.
- `results.json`: a compact record with `review_id`, `included_article_ids`,
  `retrieved_article_ids`, unmatched included IDs or entries, model token
  counts, and numeric behavior counts. No derived unmatched-item count is
  supplied; the evaluator deduplicates the two unmatched lists.

The compact records contain the fields required by the public evaluator. The
reports are model outputs and may contain errors; their literature links are
part of the original output.

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
