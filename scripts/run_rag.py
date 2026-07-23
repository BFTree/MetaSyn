#!/usr/bin/env python3
"""Run one-pass actual or oracle MetaSyn RAG for one review."""

import argparse
import json
from pathlib import Path

from dotenv import load_dotenv

from metasyn.data import load_corpus, review_by_id
from metasyn.query import build_protocol_query
from metasyn.rag import build_prompt, extract_included_articles, generate_report
from metasyn.retrieval import DEFAULT_MODEL, Retriever
from metasyn.sparse import BM25Retriever


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-id", type=int, required=True)
    parser.add_argument("--index")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--top-k", type=int, default=200)
    parser.add_argument("--mode", choices=("actual", "oracle"), default="actual")
    parser.add_argument(
        "--retriever",
        choices=("bm25", "dense_raw", "ma_retriever"),
        default="ma_retriever",
    )
    parser.add_argument("--dataset", default="THUIR/MetaSyn")
    parser.add_argument("--retriever-model")
    parser.add_argument("--llm-model")
    parser.add_argument("--device")
    args = parser.parse_args()

    review = review_by_id(args.review_id, args.dataset)
    corpus = load_corpus(args.dataset)
    if args.retriever == "bm25":
        if args.mode == "oracle":
            raise ValueError("Oracle diagnostics use MA-Retriever")
        candidates = BM25Retriever(corpus).search(review, args.top_k)
    else:
        if not args.index:
            raise ValueError("--index is required for dense retrieval")
        if args.mode == "oracle" and args.retriever != "ma_retriever":
            raise ValueError("Oracle diagnostics use MA-Retriever")
        retriever_model = args.retriever_model or (
            "BAAI/bge-large-en-v1.5"
            if args.retriever == "dense_raw"
            else DEFAULT_MODEL
        )
        retriever = Retriever(corpus, args.index, retriever_model, args.device)
        candidates = (
            retriever.search_oracle(review, args.top_k)
            if args.mode == "oracle"
            else retriever.search(review, args.top_k)
        )
    prompt = build_prompt(review, candidates)
    report, usage = generate_report(prompt, args.llm_model)
    extraction = extract_included_articles(report, candidates)

    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "report.md").write_text(report + "\n", encoding="utf-8")
    result = {
        "review_id": args.review_id,
        "mode": args.mode,
        "retriever": args.retriever,
        "query": build_protocol_query(review),
        "retrieved_article_ids": [row["corpus_id"] for row in candidates],
        "retrieved_articles": candidates,
        **extraction,
        "usage": usage,
    }
    (args.output / "results.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
