import yaml
import structlog
from pathlib import Path
from dataclasses import dataclass
from jsonschema import Draft202012Validator

CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "app_name": {"type": "string"},
        "debug": {"type": "boolean"},
        "log_level": {"type": "string"},
    },
    "required": ["app_name", "debug", "log_level"],
}

@dataclass
class Settings:
    app_name: str
    debug: bool
    log_level: str

def load_yaml_config(path: str) -> Settings:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError("Config file not found")

    with open(file_path, "r") as f:
        data = yaml.safe_load(f)

    validator = Draft202012Validator(CONFIG_SCHEMA)
    validator.validate(data)

    settings = Settings(**data)

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer()
        ]
    )

    return settings
