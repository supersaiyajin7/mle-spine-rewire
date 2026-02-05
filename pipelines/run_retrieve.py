from pipelines.retrieve import retrieve

results = retrieve(
    query="test query",
    model_name="fake-embedder",
    version="v1"
)

for r in results:
    print(r.chunk_id, r.score)
