from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class MockLynkMeshAdapter:
    """Loads LynkMesh-style graph-backed impact context from a fixture."""

    def __init__(self, fixture_path: str | Path) -> None:
        self.fixture_path = Path(fixture_path)

    def load_context(self) -> dict[str, Any]:
        with self.fixture_path.open("r", encoding="utf-8") as f:
            return json.load(f)
