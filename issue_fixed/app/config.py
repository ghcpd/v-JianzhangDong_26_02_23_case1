import yaml
import structlog
from pathlib import Path
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


def load_yaml_config(path: str) -> dict:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError("Config file not found")

    with open(file_path, "r") as f:
        data = yaml.safe_load(f)

    validator = Draft202012Validator(CONFIG_SCHEMA)
    validator.validate(data)

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer()
        ]
    )

    return data
