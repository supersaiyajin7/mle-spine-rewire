# I have created this to reflect on the work I have done so far - and what I can take away from this, like a small personal blog.

# 01-Feb-2026 - CONFIG SPINE
What config change should never be allowed at runtime?
- Appconfig is something which needs to be core for me. Rest can also be considered to be static, but hotswapping is possible.(it is called - SYSTEM INVARIANTS)

What config change is safe to hot-reload?
- Behavioral configuration such as prompt templates, retrieval parameters, and bounded model parameters, as long as input/output contracts and SLOs are preserved

What’s the blast radius of a bad prompt config?
- Inference quality , but affects trust, latency and cost. They degrade systems silently.


# 02-Feb-2026 
I realized idempotency should be handled via lookup before object creation, not after.

Why did I choose character-based chunking?
We chose character-based chunking because it is deterministic, tokenizer-agnostic, and reproducible across runs and environments.

What breaks if I change chunk size?
Chunk size changes don’t cause hard failures, but they invalidate retrieval assumptions, embedding distributions, and cached artifacts. That’s why chunk size is a configuration change with real blast radius

What downstream components assume chunk stability?
Any component that relies on chunks as stable units of meaning.
Downstream components such as embedding generation, vector indexing, retrieval scoring, prompt assembly, cost estimation, and debugging pipelines all assume chunk boundaries are stable. Changing chunking invalidates embeddings, indices, cached results, and traceability.

# 04-Feb-2026
What changes require regenerating embeddings?
-Embeddings must be regenerated whenever the semantic input to the embedding function changes.

What changes do not require regeneration?
Changes that do not affect the text passed to the embedding function do not require regeneration.
Does NOT require regeneration :: metadata-only changes (tags, source, owner), indexing strategy changes (later), retrieval logic changes

Why is embedding versioning non-optional?
Without versioning, embeddings become untraceable, unreproducible artifacts that cannot be debugged, audited, or safely migrated.

One thing which surprised me ?
- i was used to langchain doing the heavy lifting for me - but the contracts were not clear as it makes it easy for us - this method makes us actually understand the fundamentals, and help us trace back to the embeddings/identify the root cause. Now even with langchain, I can try to design my contracts with clarity.

# 05-Feb-2026
What assumptions does this retrieval logic make?
- This retrieval logic assumes that chunk boundaries are stable, embeddings were generated using the same model and version, and similarity scores are comparable across all stored embeddings.

What changes invalidate retrieval results?
-Retrieval results are invalidated by any change to chunk content, chunk boundaries, embedding model/version, or embedding generation logic.

Why is explainability more important than speed here?
Explainability is more important than speed because retrieval errors cause silent failures that manifest as hallucinations, not crashes.
