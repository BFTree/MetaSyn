"""
Semantic Similarity using Sentence Transformers.

Uses a high-quality embedding model for semantic similarity computation.
"""

from typing import List, Optional, Dict
import numpy as np


class SemanticSimilarity:
    """
    Computes semantic similarity between text pairs using sentence transformers.

    Model: paraphrase-multilingual-mpnet-base-v2
    - High quality for semantic textual similarity
    - Supports multiple languages
    - Good for short text (phrases, sentences)
    """

    _model = None

    @classmethod
    def get_model(cls):
        """Lazy load the model."""
        if cls._model is None:
            try:
                from sentence_transformers import SentenceTransformer
                cls._model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
            except ImportError:
                raise ImportError("Please install sentence-transformers: pip install sentence-transformers")
        return cls._model

    @classmethod
    def compute_pairwise_similarity(cls, texts_a: List[str], texts_b: List[str]) -> np.ndarray:
        """
        Compute pairwise cosine similarity between two lists of texts.

        Args:
            texts_a: List of texts (e.g., GT criteria)
            texts_b: List of texts (e.g., extracted criteria)

        Returns:
            Similarity matrix of shape (len(texts_a), len(texts_b))
        """
        if not texts_a or not texts_b:
            return np.array([]).reshape(len(texts_a), len(texts_b))

        model = cls.get_model()

        # Compute embeddings
        embeddings_a = model.encode(texts_a, convert_to_numpy=True, normalize_embeddings=True)
        embeddings_b = model.encode(texts_b, convert_to_numpy=True, normalize_embeddings=True)

        # Cosine similarity (dot product since normalized)
        similarity_matrix = np.dot(embeddings_a, embeddings_b.T)

        return similarity_matrix

    @classmethod
    def compute_soft_recall_precision_f1(
        cls,
        gt_items: List[str],
        extracted_items: List[str],
        threshold: float = 0.3
    ) -> Dict[str, float]:
        """
        Compute soft recall, precision, F1 using semantic similarity.

        Recall: For each GT item, what's the max similarity to any extracted item?
        Precision: For each extracted item, what's the max similarity to any GT item?

        Args:
            gt_items: Ground truth items (e.g., criteria)
            extracted_items: Extracted items from report
            threshold: Minimum similarity threshold

        Returns:
            Dictionary with soft_recall, soft_precision, soft_f1
        """
        if not gt_items:
            return {"soft_recall": None, "soft_precision": None, "soft_f1": None}

        if not extracted_items:
            return {"soft_recall": 0.0, "soft_precision": 0.0, "soft_f1": 0.0}

        # Compute similarity matrix
        similarity_matrix = cls.compute_pairwise_similarity(gt_items, extracted_items)

        if similarity_matrix.size == 0:
            return {"soft_recall": 0.0, "soft_precision": 0.0, "soft_f1": 0.0}

        # Soft recall: for each GT item, max similarity to any extracted
        # Average over all GT items
        gt_max_similarities = np.max(similarity_matrix, axis=1)  # Shape: (len(gt_items),)
        soft_recall = np.mean(gt_max_similarities)

        # Soft precision: for each extracted item, max similarity to any GT
        # Average over all extracted items
        ext_max_similarities = np.max(similarity_matrix, axis=0)  # Shape: (len(extracted),)
        soft_precision = np.mean(ext_max_similarities)

        # F1
        if soft_precision + soft_recall > 0:
            soft_f1 = 2 * soft_precision * soft_recall / (soft_precision + soft_recall)
        else:
            soft_f1 = 0.0

        return {
            "soft_recall": round(float(soft_recall), 4),
            "soft_precision": round(float(soft_precision), 4),
            "soft_f1": round(float(soft_f1), 4),
            "num_gt_items": len(gt_items),
            "num_extracted_items": len(extracted_items)
        }

    @classmethod
    def compute_single_similarity(cls, text_a: str, text_b: str) -> float:
        """
        Compute similarity between two single texts.

        Args:
            text_a: First text
            text_b: Second text

        Returns:
            Cosine similarity (0-1)
        """
        if not text_a or not text_b:
            return 0.0

        model = cls.get_model()
        emb_a = model.encode(text_a, convert_to_numpy=True, normalize_embeddings=True)
        emb_b = model.encode(text_b, convert_to_numpy=True, normalize_embeddings=True)

        return float(np.dot(emb_a, emb_b))
