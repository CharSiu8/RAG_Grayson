# ================================================================================
# WHAT THIS FILE IS:
# Embeddings wrapper for converting text to vector representations.
#
# WHY YOU NEED IT:
# - Converts text into semantic vectors for similarity search
# - Uses sentence-transformers for high-quality embeddings
# - Enables semantic search in the vector database
# - Lazy-loads the model to optimize startup time
# ================================================================================

"""Embeddings helper using sentence-transformers.
"""
from typing import List
from sentence_transformers import SentenceTransformer

from .config import get_settings

SETTINGS = get_settings()


_MODEL = None


def get_model():
    global _MODEL
    if _MODEL is None:
        _MODEL = SentenceTransformer(SETTINGS.embedding_model)
    return _MODEL


def embed_texts(texts: List[str]):
    model = get_model()
    return model.encode(texts, show_progress_bar=False, convert_to_numpy=True)
