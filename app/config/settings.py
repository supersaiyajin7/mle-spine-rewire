from pydantic import BaseModel


class ChunkingConfig(BaseModel):
    chunk_size: int = 5000
    overlap: int = 50


class EmbeddingConfig(BaseModel):
    model_name: str = "fake-embedder"
    version: str = "v2"
    dimension: int = 8


class RetrievalConfig(BaseModel):
    top_k: int = 3
    similarity_threshold: float = 0.0


class GenerationConfig(BaseModel):
    max_tokens: int = 256
    temperature: float = 0.2


class AppConfig(BaseModel):
    chunking: ChunkingConfig = ChunkingConfig()
    embedding: EmbeddingConfig = EmbeddingConfig()
    retrieval: RetrievalConfig = RetrievalConfig()
    generation: GenerationConfig = GenerationConfig()


settings = AppConfig()