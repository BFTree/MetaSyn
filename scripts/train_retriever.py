#!/usr/bin/env python3
"""Fine-tune MA-Retriever without test-article positives."""

import argparse
import random

import numpy as np
import torch
from sentence_transformers import InputExample, SentenceTransformer, losses
from sentence_transformers.datasets import NoDuplicatesDataLoader

from metasyn.data import load_corpus, load_reviews
from metasyn.query import retrieval_query
from metasyn.retrieval import document_text


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-model", default="BAAI/bge-large-en-v1.5")
    parser.add_argument("--dataset", default="THUIR/MetaSyn")
    parser.add_argument("--output", required=True)
    parser.add_argument("--epochs", type=int, default=1)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=2e-5)
    parser.add_argument("--seed", type=int, default=718)
    args = parser.parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    train_reviews = load_reviews("train", args.dataset)
    test_reviews = load_reviews("test", args.dataset)
    corpus = load_corpus(args.dataset)
    positions = {
        int(corpus_id): position for position, corpus_id in enumerate(corpus["ID"])
    }
    test_article_ids = {
        int(corpus_id)
        for review in test_reviews
        for corpus_id in review.get("matched_corpus_ids") or []
    }
    examples = []
    for review in train_reviews:
        query = retrieval_query(dict(review))
        for corpus_id in review.get("matched_corpus_ids") or []:
            corpus_id = int(corpus_id)
            if corpus_id in test_article_ids or corpus_id not in positions:
                continue
            examples.append(
                InputExample(texts=[query, document_text(dict(corpus[positions[corpus_id]]))])
            )
    loader = NoDuplicatesDataLoader(examples, batch_size=args.batch_size)
    model = SentenceTransformer(args.base_model)
    model.max_seq_length = 512
    loss = losses.MultipleNegativesRankingLoss(model=model, scale=20.0)
    warmup_steps = max(1, round(len(loader) * args.epochs * 0.1))
    model.fit(
        train_objectives=[(loader, loss)],
        epochs=args.epochs,
        warmup_steps=warmup_steps,
        optimizer_params={"lr": args.learning_rate},
        use_amp=torch.cuda.is_available(),
        show_progress_bar=True,
    )
    model.save(args.output)


if __name__ == "__main__":
    main()
