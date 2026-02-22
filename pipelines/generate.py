
from app.core.contracts import GenerationRequest, GenerationResponse


def build_prompt(query: str, contexts: list[str]) -> str:
    context_block = "\n\n".join(contexts)

    prompt = f"""
You are a system that answers questions strictly using the provided context.
If the answer cannot be found in the context, say "I don't know".

Context:
{context_block}

Question:
{query}

Answer:
""".strip()

    return prompt


def fake_llm(prompt: str) -> str:
    return "FAKE ANSWER BASED ON PROVIDED CONTEXT"


def generate_answer(req: GenerationRequest) -> GenerationResponse:
    prompt = build_prompt(req.query, req.contexts)

    answer = fake_llm(prompt)

    return GenerationResponse(
        answer=answer,
        used_contexts=req.contexts
    )

