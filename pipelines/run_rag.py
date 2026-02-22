from pipelines.rag import rag_pipeline

resp = rag_pipeline(
    query="What is machine learning?",
    model_name="fake-embedder",
    embedding_version="v2",
)

print("Refused:", resp.refused)
print("Reason:", resp.reason)
print("Answer:", resp.answer)
print("Contexts:", resp.used_contexts)
