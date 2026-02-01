# I have created this to reflect on the work I have done so far - and what I can take away from this, like a small personal blog.

# 01-Feb-2026 - CONFIG SPINE
What config change should never be allowed at runtime?
- Appconfig is something which needs to be core for me. Rest can also be considered to be static, but hotswapping is possible.(it is called - SYSTEM INVARIANTS)

What config change is safe to hot-reload?
- Behavioral configuration such as prompt templates, retrieval parameters, and bounded model parameters, as long as input/output contracts and SLOs are preserved

What’s the blast radius of a bad prompt config?
- Inference quality , but affects trust, latency and cost. They degrade systems silently.


