from pipelines.embed import generate_embedding, save_embedding
from pipelines.chunk import chunk_text

sample_text = "A" * 1000

chunks = chunk_text(
    document_id="doc_123",
    text=sample_text,
    metadata={"source": "test"}
)

for c in chunks:
    emb = generate_embedding(
        text=c.content,
        chunk_id=c.chunk_id,
        document_id=c.document_id,
        model_name="fake-embedder",
        version="v1"
    )
    save_embedding(emb)
