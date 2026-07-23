#!/usr/bin/env python3
"""Build the public MA-Retriever FAISS index."""

import argparse

from metasyn.data import load_corpus
from metasyn.retrieval import DEFAULT_MODEL, build_index


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    parser.add_argument("--dataset", default="THUIR/MetaSyn")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--device")
    args = parser.parse_args()
    build_index(
        load_corpus(args.dataset),
        args.output,
        args.model,
        args.batch_size,
        args.device,
    )


if __name__ == "__main__":
    main()

