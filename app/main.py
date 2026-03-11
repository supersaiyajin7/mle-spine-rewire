from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel

from app.core.config import ConfigLoader
from pipelines.rag import rag_pipeline
from app.config.settings import settings
from app.observability.logging import get_logger


# Load config at startup
loader = ConfigLoader(Path("config"))
cfg = loader.load()

app = FastAPI(title="MLE Spine RAG Service")


class QueryRequest(BaseModel):
    query: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/query")
def query_rag(req: QueryRequest):

    response = rag_pipeline(
        query=req.query,
        model_name=settings.embedding.model_name,
        embedding_version=settings.embedding.version,
    )
    logger = get_logger("main")
    logger.info(f"Received query: {req.query}")
    logger.info(f"Refused:{response.refused}")
    return response


# Optional CLI mode for debugging
if __name__ == "__main__":
    print("Config loaded successfully")
    print(cfg)