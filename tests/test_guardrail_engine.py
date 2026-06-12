from app.adapters.lynkmesh_adapter import MockLynkMeshAdapter
from app.adapters.orbit_adapter import MockOrbitAdapter
from app.guardrails.engine import GuardrailEngine


def test_detects_controller_to_model_bypass():
    orbit_context = MockOrbitAdapter("app/fixtures/orbit_context.json").load_context()
    lynkmesh_context = MockLynkMeshAdapter("app/fixtures/lynkmesh_impact_context.json").load_context()

    violations = GuardrailEngine().evaluate(orbit_context, lynkmesh_context)

    assert len(violations) == 1
    assert violations[0].rule_id == "layering.controller_to_model_bypass"
    assert violations[0].source == "InvoiceController::store"
    assert violations[0].target == "InvoiceModel::create"
