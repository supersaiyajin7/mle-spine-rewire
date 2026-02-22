from pipelines.retrieve import retrieve
from pipelines.generate import generate_answer
from app.core.contracts import GenerationRequest, RAGResponse


def rag_pipeline(
    query: str,
    model_name: str,
    embedding_version: str,
    top_k: int = 3,
) -> RAGResponse:

    retrieval_results = retrieve(
        query=query,
        model_name=model_name,
        version=embedding_version,
        top_k=top_k,
    )

    # Failure containment: no context
    if not retrieval_results:
        return RAGResponse(
            answer=None,
            used_contexts=[],
            refused=True,
            reason="No relevant context found",
        )

    contexts = [r.content for r in retrieval_results]

    gen_req = GenerationRequest(
        query=query,
        contexts=contexts,
        max_tokens=256,
        temperature=0.2,
    )

    gen_resp = generate_answer(gen_req)

    return RAGResponse(
        answer=gen_resp.answer,
        used_contexts=gen_resp.used_contexts,
        refused=False,
        reason=None,
    )
