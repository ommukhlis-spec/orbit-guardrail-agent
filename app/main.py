from __future__ import annotations

import argparse
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from app.adapters.gitlab_mr_adapter import LocalMRCommentAdapter
from app.adapters.lynkmesh_adapter import MockLynkMeshAdapter
from app.adapters.orbit_adapter import MockOrbitAdapter
from app.briefing.renderer import render_mr_briefing
from app.guardrails.engine import GuardrailEngine

DEFAULT_ORBIT_FIXTURE = Path("app/fixtures/orbit_context.json")
DEFAULT_LYNKMESH_FIXTURE = Path("app/fixtures/lynkmesh_impact_context.json")
DEFAULT_OUTPUT = Path("demo/sample_mr_comment.md")
LOG_DIR = Path("app/logs")


def run_mock(orbit_fixture: Path, lynkmesh_fixture: Path, output: Path) -> dict[str, object]:
    orbit_context = MockOrbitAdapter(orbit_fixture).load_context()
    lynkmesh_context = MockLynkMeshAdapter(lynkmesh_fixture).load_context()
    violations = GuardrailEngine().evaluate(orbit_context, lynkmesh_context)
    body = render_mr_briefing(orbit_context, lynkmesh_context, violations)
    comment_path = LocalMRCommentAdapter(output).post_comment(body)

    run_id = str(uuid.uuid4())
    run_log = {
        "run_id": run_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "mode": "mock",
        "project_id": orbit_context.get("project_id"),
        "merge_request_iid": orbit_context.get("merge_request_iid"),
        "orbit_context_id": orbit_context.get("orbit_context", {}).get("context_id", "orbit-demo-context-001"),
        "lynkmesh_context_pack_id": lynkmesh_context.get("context_pack_id"),
        "rules_evaluated": ["layering.controller_to_model_bypass"],
        "violations": [v.__dict__ for v in violations],
        "blast_radius_count": len(lynkmesh_context.get("blast_radius", [])),
        "comment_posted": True,
        "comment_output_path": str(comment_path),
    }
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / f"run_{run_id}.json"
    log_path.write_text(json.dumps(run_log, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    run_log["log_path"] = str(log_path)
    return run_log


def main() -> None:
    parser = argparse.ArgumentParser(description="Orbit Guardrail Agent")
    parser.add_argument("--mode", choices=["mock"], default="mock")
    parser.add_argument("--orbit-fixture", default=str(DEFAULT_ORBIT_FIXTURE))
    parser.add_argument("--lynkmesh-fixture", default=str(DEFAULT_LYNKMESH_FIXTURE))
    parser.add_argument("--out", default=str(DEFAULT_OUTPUT))
    args = parser.parse_args()

    if args.mode != "mock":
        raise SystemExit("Only mock mode is implemented in the current MVP.")

    run_log = run_mock(Path(args.orbit_fixture), Path(args.lynkmesh_fixture), Path(args.out))
    print(json.dumps(run_log, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
