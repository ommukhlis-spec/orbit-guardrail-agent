from pathlib import Path


def test_stage5_docs_exist():
    assert Path("docs/stage5_gitlab_real_mr_prep.md").is_file()
    assert Path("demo/gitlab_real_mr_checklist.md").is_file()
    assert Path("demo/evidence/gitlab_real_mr_evidence_template.md").is_file()
    assert Path("scripts/prepare_real_mr_demo.ps1").is_file()


def test_stage5_docs_contain_safe_gitlab_flow():
    doc = Path("docs/stage5_gitlab_real_mr_prep.md").read_text(encoding="utf-8")
    assert "--dry-run" in doc
    assert "GITLAB_TOKEN" in doc
    assert "Do not claim yet" in doc
    assert "AI Catalog" in doc


def test_stage5_checklist_mentions_demo_violation():
    checklist = Path("demo/gitlab_real_mr_checklist.md").read_text(encoding="utf-8")
    assert "demo/controller-model-bypass" in checklist
    assert "InvoiceModel::create" in checklist
    assert "GitLab API live mode" in checklist
