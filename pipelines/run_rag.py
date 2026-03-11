from pipelines.rag import rag_pipeline
from app.config.settings import settings


resp = rag_pipeline(
    query="What is machine learning?",
    model_name=settings.embedding.model_name,
    embedding_version=settings.embedding.version,
)

print("Refused:", resp.refused)
print("Reason:", resp.reason)
print("Answer:", resp.answer)
print("Contexts:", resp.used_contexts)
