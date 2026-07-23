#!/usr/bin/env python3
"""Run leakage-safe MA-Retriever search for one MetaSyn review."""

import argparse
import json
from pathlib import Path

from metasyn.data import load_corpus, review_by_id
from metasyn.query import build_protocol_query
from metasyn.retrieval import DEFAULT_MODEL, Retriever
from metasyn.sparse import BM25Retriever


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-id", type=int, required=True)
    parser.add_argument(
        "--retriever", choices=("bm25", "dense_raw", "ma_retriever"),
        default="ma_retriever",
    )
    parser.add_argument("--index")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--top-k", type=int, default=200)
    parser.add_argument("--dataset", default="THUIR/MetaSyn")
    parser.add_argument("--model")
    parser.add_argument("--device")
    args = parser.parse_args()
    review = review_by_id(args.review_id, args.dataset)
    corpus = load_corpus(args.dataset)
    if args.retriever == "bm25":
        retriever = BM25Retriever(corpus)
    else:
        if not args.index:
            parser.error("--index is required for a dense retriever")
        model = args.model or (
            "BAAI/bge-large-en-v1.5"
            if args.retriever == "dense_raw"
            else DEFAULT_MODEL
        )
        retriever = Retriever(corpus, args.index, model, args.device)
    candidates = retriever.search(review, args.top_k)
    payload = {
        "review_id": args.review_id,
        "query": build_protocol_query(review),
        "retrieved_article_ids": [row["corpus_id"] for row in candidates],
        "retrieved_articles": candidates,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
