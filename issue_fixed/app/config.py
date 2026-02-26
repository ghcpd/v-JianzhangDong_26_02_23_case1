from pathlib import Path
from typing import Any, Dict

import structlog
import yaml
from jsonschema import Draft202012Validator
from packaging.version import Version
from pydantic import __version__ as pydantic_version

IS_PYDANTIC_V2 = Version(pydantic_version) >= Version("2.0")

# Compatibility: prefer pydantic-settings if installed; fallback to pydantic.BaseSettings
try:  # pydantic-settings installed (pydantic v2)
    from pydantic_settings import BaseSettings  # type: ignore
except ImportError:  # pydantic v1 fallback
    from pydantic import BaseSettings  # type: ignore

CONFIG_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "properties": {
        "app_name": {"type": "string"},
        "debug": {"type": "boolean"},
        "log_level": {"type": "string"},
    },
    "required": ["app_name", "debug", "log_level"],
}


class Settings(BaseSettings):
    app_name: str
    debug: bool
    log_level: str

    if IS_PYDANTIC_V2:
        model_config = {
            "env_prefix": "SMART_",
            "case_sensitive": False,
        }
    else:
        class Config:  # type: ignore[override]
            env_prefix = "SMART_"
            case_sensitive = False


def load_yaml_config(path: str | Path) -> Settings:
    """
    Load YAML configuration, validate against JSON Schema, and return Settings.
    """

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    validator = Draft202012Validator(CONFIG_SCHEMA)
    validator.validate(data)

    settings = Settings(**data)

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ]
    )

    return settings
