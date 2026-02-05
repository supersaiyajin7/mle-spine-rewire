from pathlib import Path
from app.core.contracts import Document, compute_document_id
import json


RAW_DIR = Path("storage/raw")
PROCESSED_DIR = Path("storage/processed")
REJECTED_DIR = Path("storage/rejected")

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
REJECTED_DIR.mkdir(parents=True, exist_ok=True)


def load_existing_document(path: Path) -> Document:
    return Document.model_validate_json(path.read_text())


def ingest_document(source: str, content: str, metadata: dict):
    document_id = compute_document_id(source, content)

    processed_path = PROCESSED_DIR / f"{document_id}.json"
    raw_path = RAW_DIR / f"{document_id}.json"
    
    # Idempotency check FIRST
    if processed_path.exists():
        return load_existing_document(processed_path)


    try:
        doc = Document(
            document_id=document_id,
            source=source,
            content=content,
            metadata=metadata
        )
    except Exception as e:
        REJECTED_DIR.joinpath(f"{document_id}.json").write_text(
            json.dumps({"error": str(e)})
        )
        return None

    raw_path.write_text(doc.model_dump_json())
    processed_path.write_text(doc.model_dump_json())

    return doc
