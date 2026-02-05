from pathlib import Path
from app.core.contracts import Embedding, RetrievalResult
from typing import List
from pipelines.embed import generate_embedding


EMBEDDING_DIR = Path("storage/embeddings")


def load_embeddings() -> List[Embedding]:
    embeddings = []
    for path in EMBEDDING_DIR.glob("*.json"):
        embeddings.append(
            Embedding.model_validate_json(path.read_text())
        )
    return embeddings


def dot_product(v1: List[float], v2: List[float]) -> float:
    return sum(a * b for a, b in zip(v1, v2))


def retrieve(
    query: str,
    model_name: str,
    version: str,
    top_k: int = 3
) -> List[RetrievalResult]:

    query_embedding = generate_embedding(
        text=query,
        chunk_id="query",
        document_id="query",
        model_name=model_name,
        version=version
    )

    embeddings = load_embeddings()
    scored = []

    for emb in embeddings:
        score = dot_product(query_embedding.vector, emb.vector)
        scored.append((score, emb))

    scored.sort(key=lambda x: x[0], reverse=True)

    results = []
    for score, emb in scored[:top_k]:
        results.append(
            RetrievalResult(
                chunk_id=emb.chunk_id,
                document_id=emb.document_id,
                score=score,
                content=f"[chunk {emb.chunk_id}]"
            )
        )

    return results
