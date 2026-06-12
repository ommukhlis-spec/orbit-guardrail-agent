from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class MockOrbitAdapter:
    """Loads GitLab Orbit-style context from a fixture.

    This adapter intentionally uses local JSON fixtures for the first MVP so the
    guardrail logic can be tested without depending on platform provisioning.
    """

    def __init__(self, fixture_path: str | Path) -> None:
        self.fixture_path = Path(fixture_path)

    def load_context(self) -> dict[str, Any]:
        with self.fixture_path.open("r", encoding="utf-8") as f:
            return json.load(f)
