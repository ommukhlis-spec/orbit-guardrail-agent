from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GuardrailRule:
    rule_id: str
    title: str
    expected_flow: str
    detected_flow: str
    severity: str = "warning"


CONTROLLER_TO_MODEL_BYPASS = GuardrailRule(
    rule_id="layering.controller_to_model_bypass",
    title="Controller should not directly access Model when a Service layer exists",
    expected_flow="Controller → Service → Model",
    detected_flow="Controller → Model",
)
