"""Shared paths and configuration.

Settings are read from ``config`` in the project root when it exists, otherwise from
``default.config``; secrets likewise from ``secret`` or ``default.secret``. Copy the
defaults to ``config`` / ``secret`` to change them locally; neither copy is in git.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load_config(root: Path = PROJECT_ROOT) -> dict[str, Any]:
    """Return the study configuration, preferring a local ``config`` over ``default.config``."""
    local = root / "config"
    path = local if local.exists() else root / "default.config"
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def load_secret(root: Path = PROJECT_ROOT) -> dict[str, Any]:
    """Return the secrets from ``secret``, or the empty template ``default.secret``."""
    local = root / "secret"
    path = local if local.exists() else root / "default.secret"
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def resolve(path: str | Path, root: Path = PROJECT_ROOT) -> Path:
    """Resolve a config path relative to the project root."""
    path = Path(path)
    return path if path.is_absolute() else root / path


def load_properties(config: dict[str, Any], root: Path = PROJECT_ROOT,
                    screened_only: bool = True) -> list[dict[str, Any]]:
    """Return the candidate properties, by default only those that passed screening."""
    with resolve(config["properties"], root).open(encoding="utf-8") as fh:
        properties = json.load(fh)["properties"]
    ids = [p["id"] for p in properties]
    if len(ids) != len(set(ids)):
        raise ValueError("property ids in the properties file must be unique")
    if screened_only:
        properties = [p for p in properties if p.get("screened_in", True)]
    return properties


def load_scenes(config: dict[str, Any], root: Path = PROJECT_ROOT) -> list[dict[str, Any]]:
    with resolve(config["scenes"], root).open(encoding="utf-8") as fh:
        return json.load(fh)["scenes"]
