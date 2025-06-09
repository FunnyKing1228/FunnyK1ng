"""Minimal YAML loader supporting simple key/value and list syntax."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


def _parse_value(val: str) -> Any:
    """Parse a scalar YAML value to python type."""
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        return [_parse_value(v.strip()) for v in inner.split(",")] if inner else []
    try:
        return int(val)
    except ValueError:
        try:
            return float(val)
        except ValueError:
            return val


def load_yaml(path: str | Path) -> Dict[str, Any]:
    """Load a very small subset of YAML into a dictionary.

    This loader only supports mappings of scalars and lists and is
    intended for the simple config files in this repository.
    """
    path = Path(path)
    data: Dict[str, Any] = {}
    current_key: str | None = None
    for raw in path.read_text().splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - "):
            if current_key is None:
                raise ValueError("List item outside of a key")
            data.setdefault(current_key, []).append(_parse_value(line[4:].strip()))
        elif line.endswith(":"):
            current_key = line[:-1].strip()
            data[current_key] = []
        else:
            current_key = None
            if ":" not in line:
                raise ValueError(f"Invalid line: {line}")
            key, val = line.split(":", 1)
            data[key.strip()] = _parse_value(val.strip())
    return data


__all__ = ["load_yaml"]
