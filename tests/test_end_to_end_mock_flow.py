from pathlib import Path

from app.main import run_mock


def test_end_to_end_mock_flow_writes_comment_and_log(tmp_path, monkeypatch):
    output = tmp_path / "sample_mr_comment.md"
    monkeypatch.chdir(Path(__file__).resolve().parents[1])

    run_log = run_mock(
        Path("app/fixtures/orbit_context.json"),
        Path("app/fixtures/lynkmesh_impact_context.json"),
        output,
    )

    assert output.exists()
    assert "Orbit Guardrail Briefing" in output.read_text(encoding="utf-8")
    assert run_log["comment_posted"] is True
    assert run_log["blast_radius_count"] == 3
    assert Path(str(run_log["log_path"])).exists()
