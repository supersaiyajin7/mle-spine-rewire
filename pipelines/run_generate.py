from app.core.contracts import GenerationRequest
from pipelines.generate import generate_answer

req = GenerationRequest(
    query="What is machine learning?",
    contexts=[
        "Machine learning is a field of computer science that focuses on data-driven models.",
        "It enables systems to learn from data."
    ],
    max_tokens=100,
    temperature=0.2
)

resp = generate_answer(req)

print(resp.answer)
