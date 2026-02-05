from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from datetime import datetime
import uuid
import hashlib


def compute_document_id(source: str, content: str) -> str:
    raw = f"{source}:{content}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


class Document(BaseModel):
    document_id: str
    source: str
    content: str
    metadata: Dict[str, str]
    ingested_at: datetime = Field(default_factory=datetime.utcnow)


class Chunk(BaseModel):
    chunk_id: str
    document_id: str
    content: str
    metadata: Dict[str, str]
    chunk_index: int
    created_at: datetime

class Embedding(BaseModel):
    chunk_id: str
    document_id: str
    vector: List[float]
    model_name: str
    embedding_version: str
    created_at: datetime

class RetrievalResult(BaseModel):
    chunk_id: str
    document_id: str
    score: float
    content: str
