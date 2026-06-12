import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def test_stage4_evidence_files_exist():
    expected = [
        "demo/evidence/README.md",
        "demo/evidence/demo_run_log.redacted.json",
        "demo/evidence/context_evidence_matrix.md",
        "demo/evidence/submission_checklist.md",
        "demo/video_shot_list.md",
        "docs/stage4_evidence_artifacts.md",
    ]
    for rel in expected:
        assert (ROOT / rel).exists(), rel


def test_redacted_run_log_is_public_safe():
    payload = json.loads(read("demo/evidence/demo_run_log.redacted.json"))
    assert payload["mode"] == "mock"
    assert payload["safety"]["uses_real_customer_data"] is False
    assert payload["safety"]["contains_tokens_or_secrets"] is False
    assert payload["safety"]["contains_llm_inference"] is False
    assert payload["safety"]["production_ready_ci_enforcement"] is False
    assert payload["violations"][0]["rule_id"] == "layering.controller_to_model_bypass"


def test_submission_checklist_keeps_pending_claims_separate():
    checklist = read("demo/evidence/submission_checklist.md")
    assert "Do not claim full GitLab Orbit integration until connected" in checklist
    assert "Do not claim LynkMesh replaces GitLab Orbit" in checklist
    assert "AI Catalog" in checklist


def test_video_shot_list_has_three_minute_plan():
    shot_list = read("demo/video_shot_list.md")
    assert "3-Minute Demo Video Shot List" in shot_list
    assert "0:00" in shot_list
    assert "3:00" in shot_list
    assert "demo/sample_mr_comment.md" in shot_list
