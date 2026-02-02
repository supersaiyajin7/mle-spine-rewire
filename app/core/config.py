from pathlib import Path
import yaml
from pydantic import BaseModel, ValidationError
from typing import Dict, Any


class AppConfig(BaseModel):
    app: Dict[str, Any]
    runtime: Dict[str, Any]
    features: Dict[str, Any]


class ModelConfig(BaseModel):
    embedding: Dict[str, Any]
    llm: Dict[str, Any]


class PromptConfig(BaseModel):
    name: str
    version: str
    system_prompt: str
    user_prompt: str
    required_variables: list[str]


class RoutingConfig(BaseModel):
    rag: Dict[str, Any]
    fallback: Dict[str, Any]


def load_yaml(path: Path) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


class ConfigLoader:
    def __init__(self, config_dir: Path):
        self.config_dir = config_dir

    def load(self):
        try:
            system = AppConfig(**load_yaml(self.config_dir / "system.yaml"))
            models = ModelConfig(**load_yaml(self.config_dir / "models.yaml"))
            routing = RoutingConfig(**load_yaml(self.config_dir / "routing.yaml"))
            prompt = PromptConfig(
                **load_yaml(self.config_dir / "prompts" / "qa.yaml")
            )
        except ValidationError as e:
            raise RuntimeError(f"Invalid configuration: {e}")

        return {
            "system": system,
            "models": models,
            "routing": routing,
            "prompt": prompt,
        }
