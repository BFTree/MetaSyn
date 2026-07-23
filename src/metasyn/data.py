"""Load the public MetaSyn Hugging Face dataset."""

from __future__ import annotations

from datasets import Dataset, load_dataset


DEFAULT_DATASET = "THUIR/MetaSyn"


def load_reviews(
    split: str = "test",
    dataset_id: str = DEFAULT_DATASET,
    revision: str | None = None,
) -> Dataset:
    """Load the review-level train or test split."""
    if split not in {"train", "test"}:
        raise ValueError("Review split must be 'train' or 'test'")
    return load_dataset(dataset_id, "reviews", split=split, revision=revision)


def load_corpus(
    dataset_id: str = DEFAULT_DATASET, revision: str | None = None
) -> Dataset:
    """Load the shared PubMed candidate corpus."""
    return load_dataset(dataset_id, "corpus", split="train", revision=revision)


def review_by_id(
    review_id: int,
    dataset_id: str = DEFAULT_DATASET,
    revision: str | None = None,
) -> dict:
    """Find a review in either public split."""
    for split in ("test", "train"):
        rows = load_reviews(split, dataset_id, revision)
        matches = rows.filter(lambda row: int(row["ID"]) == int(review_id))
        if len(matches) == 1:
            return dict(matches[0])
    raise KeyError(f"Review ID {review_id} was not found")
