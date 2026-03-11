from pipelines.retrieve import retrieve
from pipelines.generate import generate_answer
from app.core.contracts import GenerationRequest, RAGResponse
from app.observability.logging import get_logger
from app.observability.metrics import Metrics
from time import time
from app.config.settings import settings


logger = get_logger("rag")

def rag_pipeline(
    query: str,
    model_name: str,
    embedding_version: str,
    top_k: int = 3,
) -> RAGResponse:

    start = time()

    if embedding_version != settings.embedding.version:
        logger.error("Embedding version mismatch")
        return RAGResponse(
            answer=None,
            used_contexts=[],
            refused=True,
            reason="Embedding version mismatch"
        )

    Metrics.total_requests += 1
    retrieval_results = retrieve(
        query=query,
        model_name=model_name,
        version=embedding_version,
        top_k=top_k,
    )

    logger.info(f"RAG Pipeline - Query: {query}")
    logger.info(f"RAG Pipeline - Retrieval Results: {len(retrieval_results)} chunks found")

    # Failure containment: no context
    if not retrieval_results:
        Metrics.retrieval_failures += 1
        Metrics.refusals += 1
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
        max_tokens=settings.generation.max_tokens,
        temperature=settings.generation.temperature,
    )

    gen_resp = generate_answer(gen_req)

    duration = time() - start
    logger.info(f"RAG latency: {duration:.2f} seconds")


    return RAGResponse(
        answer=gen_resp.answer,
        used_contexts=gen_resp.used_contexts,
        refused=False,
        reason=None,
    )
