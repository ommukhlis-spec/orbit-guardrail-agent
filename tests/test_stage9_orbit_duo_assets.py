from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_agents_md_contains_safe_framing():
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "LynkMesh does not replace GitLab Orbit" in text
    assert "Controller -> Service -> Model" in text
    assert "Do not claim real GitLab Orbit/Duo custom agent integration is complete" in text


def test_stage9_docs_exist():
    required = [
        "docs/stage9_orbit_duo_agentic_workflow.md",
        "demo/orbit_duo_prompts.md",
        "demo/evidence/orbit_duo_exploration_log.md",
        "demo/evidence/ai_catalog_submission_notes.md",
    ]
    for path in required:
        assert (ROOT / path).exists(), path


def test_ai_catalog_notes_are_conservative():
    text = (ROOT / "demo/evidence/ai_catalog_submission_notes.md").read_text(encoding="utf-8")
    assert "Current implementation proves" in text
    assert "being explored during Stage 9" in text
    assert "Architecture-aware Merge Request guardrail" in text
