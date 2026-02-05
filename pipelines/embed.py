import random
import hashlib
from datetime import datetime
from app.core.contracts import Embedding
from pathlib import Path


EMBEDDING_DIM = 8  # small on purpose
EMBEDDING_DIR = Path("storage/embeddings")
EMBEDDING_DIR.mkdir(parents=True, exist_ok=True)


def generate_embedding(text: str,chunk_id: str, document_id: str, model_name: str, version: str):
    vector = fake_embedding_from_text(text)
    
    return Embedding(
        chunk_id=chunk_id,
        document_id=document_id,
        vector=vector,
        model_name=model_name,
        embedding_version=version,
        created_at=datetime.utcnow()
    )

def save_embedding(embedding: Embedding) -> None:
    path = EMBEDDING_DIR / f"{embedding.chunk_id}.json"
    path.write_text(embedding.model_dump_json())


def fake_embedding_from_text(text: str, dim: int = EMBEDDING_DIM):
    seed = int(hashlib.sha256(text.encode()).hexdigest(), 16) % (10**8)
    random.seed(seed)
    return [random.random() for _ in range(dim)]
