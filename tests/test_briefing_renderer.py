from app.adapters.lynkmesh_adapter import MockLynkMeshAdapter
from app.adapters.orbit_adapter import MockOrbitAdapter
from app.briefing.renderer import render_mr_briefing
from app.guardrails.engine import GuardrailEngine


def test_render_mr_briefing_contains_hero_sections():
    orbit_context = MockOrbitAdapter("app/fixtures/orbit_context.json").load_context()
    lynkmesh_context = MockLynkMeshAdapter("app/fixtures/lynkmesh_impact_context.json").load_context()
    violations = GuardrailEngine().evaluate(orbit_context, lynkmesh_context)

    body = render_mr_briefing(orbit_context, lynkmesh_context, violations)

    assert "Orbit Guardrail Briefing" in body
    assert "Architecture Guardrail Violation" in body
    assert "Controller → Service → Model" in body
    assert "BillingEngine::syncInvoice" in body
    assert "Suggested Test Coverage" in body
    assert "sha256:demo-context-pack" in body
