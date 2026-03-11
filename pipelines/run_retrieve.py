from pipelines.retrieve import retrieve
from app.config.settings import settings


results = retrieve(
    query="test query",
    model_name="fake-embedder",
    version="v1",
    top_k=settings.retrieval.top_k
)

for r in results:
    print(r.chunk_id, r.score)
