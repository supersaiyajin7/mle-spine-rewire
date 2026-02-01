from pathlib import Path
from app.core.config import ConfigLoader

if __name__ == "__main__":
    loader = ConfigLoader(Path("config"))
    cfg = loader.load()
    print(cfg)
    print("Config loaded successfully")
    print(cfg["prompt"].name, cfg["prompt"].version)
