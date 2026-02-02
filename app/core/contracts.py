from pydantic import BaseModel, Field
from typing import Optional, Dict
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
