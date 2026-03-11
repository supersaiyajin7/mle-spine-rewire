from app.core.contracts import Chunk
from app.config.settings import settings
from datetime import datetime
import uuid

CHUNK_SIZE = settings.chunking.chunk_size
CHUNK_OVERLAP = settings.chunking.overlap


def chunk_text(document_id: str, text: str, metadata: dict):
    chunks = []
    start = 0
    index = 0

    while start < len(text):
        end = start + CHUNK_SIZE
        chunk_content = text[start:end]

        chunk = Chunk(
            chunk_id=str(uuid.uuid4()),
            document_id=document_id,
            content=chunk_content,
            metadata=metadata,
            chunk_index=index,
            created_at=datetime.utcnow()
        )

        chunks.append(chunk)

        start += CHUNK_SIZE - CHUNK_OVERLAP
        index += 1

    return chunks
