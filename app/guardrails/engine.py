from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from app.guardrails.rules import CONTROLLER_TO_MODEL_BYPASS


@dataclass(frozen=True)
class Violation:
    rule_id: str
    title: str
    severity: str
    file: str
    source: str
    target: str
    expected_flow: str
    detected_flow: str
    reason: str


class GuardrailEngine:
    """Evaluates deterministic architecture guardrails from graph context."""

    def evaluate(self, orbit_context: dict[str, Any], lynkmesh_context: dict[str, Any]) -> list[Violation]:
        violations: list[Violation] = []
        entity_layers = self._entity_layers(orbit_context, lynkmesh_context)
        source_paths = self._source_paths(orbit_context, lynkmesh_context)

        for edge in lynkmesh_context.get("new_edges", []):
            source = edge.get("from", "")
            target = edge.get("to", "")
            source_layer = self._layer_for_symbol(source, entity_layers)
            target_layer = self._layer_for_symbol(target, entity_layers)

            if source_layer == "controller" and target_layer == "model":
                related_service = self._find_related_service(orbit_context, source, target)
                if related_service:
                    rule = CONTROLLER_TO_MODEL_BYPASS
                    violations.append(
                        Violation(
                            rule_id=rule.rule_id,
                            title=rule.title,
                            severity=rule.severity,
                            file=source_paths.get(source, self._path_for_symbol(orbit_context, source)),
                            source=source,
                            target=target,
                            expected_flow=rule.expected_flow,
                            detected_flow=rule.detected_flow,
                            reason=f"Existing service candidate `{related_service}` is bypassed by direct model access.",
                        )
                    )

        return violations

    def _entity_layers(self, orbit_context: dict[str, Any], lynkmesh_context: dict[str, Any]) -> dict[str, str]:
        layers: dict[str, str] = {}
        for entity in orbit_context.get("orbit_context", {}).get("entities", []):
            if "id" in entity and "type" in entity:
                layers[str(entity["id"])] = str(entity["type"])
        for node in lynkmesh_context.get("changed_nodes", []):
            if "symbol" in node and "layer" in node:
                layers[str(node["symbol"])] = str(node["layer"])
        return layers

    def _source_paths(self, orbit_context: dict[str, Any], lynkmesh_context: dict[str, Any]) -> dict[str, str]:
        paths: dict[str, str] = {}
        for node in lynkmesh_context.get("changed_nodes", []):
            if "symbol" in node and "path" in node:
                paths[str(node["symbol"])] = str(node["path"])
        for entity in orbit_context.get("orbit_context", {}).get("entities", []):
            if "id" in entity and "path" in entity:
                paths[str(entity["id"])] = str(entity["path"])
        return paths

    def _layer_for_symbol(self, symbol: str, layers: dict[str, str]) -> str | None:
        if symbol in layers:
            return layers[symbol]
        # Fallback: match class prefix before ::
        prefix = symbol.split("::", 1)[0]
        if prefix in layers:
            return layers[prefix]
        lower = symbol.lower()
        if "controller" in lower:
            return "controller"
        if "service" in lower or "engine" in lower:
            return "service"
        if "model" in lower:
            return "model"
        return None

    def _find_related_service(self, orbit_context: dict[str, Any], source: str, target: str) -> str | None:
        target_domain = target.split("Model", 1)[0].split("::", 1)[0].replace("Model", "")
        source_domain = source.split("Controller", 1)[0].split("::", 1)[0].replace("Controller", "")
        candidates = [target_domain, source_domain]

        for entity in orbit_context.get("orbit_context", {}).get("entities", []):
            entity_id = str(entity.get("id", ""))
            entity_type = str(entity.get("type", ""))
            if entity_type != "service":
                continue
            if any(candidate and candidate in entity_id for candidate in candidates):
                return entity_id
        return None

    def _path_for_symbol(self, orbit_context: dict[str, Any], symbol: str) -> str:
        prefix = symbol.split("::", 1)[0]
        for entity in orbit_context.get("orbit_context", {}).get("entities", []):
            if entity.get("id") == prefix:
                return str(entity.get("path", ""))
        return ""
