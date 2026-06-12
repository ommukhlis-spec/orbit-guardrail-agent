from __future__ import annotations

import argparse
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.adapters.gitlab_mr_adapter import GitLabMRCommentAdapter, LocalMRCommentAdapter
from app.adapters.lynkmesh_adapter import MockLynkMeshAdapter
from app.adapters.orbit_adapter import MockOrbitAdapter
from app.briefing.renderer import render_mr_briefing
from app.guardrails.engine import GuardrailEngine

DEFAULT_ORBIT_FIXTURE = Path("app/fixtures/orbit_context.json")
DEFAULT_LYNKMESH_FIXTURE = Path("app/fixtures/lynkmesh_impact_context.json")
DEFAULT_OUTPUT = Path("demo/sample_mr_comment.md")
LOG_DIR = Path("app/logs")


def build_briefing(orbit_fixture: Path, lynkmesh_fixture: Path) -> tuple[dict[str, Any], dict[str, Any], list[Any], str]:
    orbit_context = MockOrbitAdapter(orbit_fixture).load_context()
    lynkmesh_context = MockLynkMeshAdapter(lynkmesh_fixture).load_context()
    violations = GuardrailEngine().evaluate(orbit_context, lynkmesh_context)
    body = render_mr_briefing(orbit_context, lynkmesh_context, violations)
    return orbit_context, lynkmesh_context, violations, body


def write_run_log(run_log: dict[str, Any]) -> dict[str, Any]:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / f"run_{run_log['run_id']}.json"
    log_path.write_text(json.dumps(run_log, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    run_log["log_path"] = str(log_path)
    return run_log


def base_run_log(
    *,
    mode: str,
    orbit_context: dict[str, Any],
    lynkmesh_context: dict[str, Any],
    violations: list[Any],
    comment_output_path: str,
) -> dict[str, Any]:
    return {
        "run_id": str(uuid.uuid4()),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "mode": mode,
        "project_id": orbit_context.get("project_id"),
        "merge_request_iid": orbit_context.get("merge_request_iid"),
        "orbit_context_id": orbit_context.get("orbit_context", {}).get("context_id", "orbit-demo-context-001"),
        "lynkmesh_context_pack_id": lynkmesh_context.get("context_pack_id"),
        "rules_evaluated": ["layering.controller_to_model_bypass"],
        "violations": [v.__dict__ for v in violations],
        "blast_radius_count": len(lynkmesh_context.get("blast_radius", [])),
        "comment_output_path": comment_output_path,
    }


def run_mock(orbit_fixture: Path, lynkmesh_fixture: Path, output: Path) -> dict[str, Any]:
    orbit_context, lynkmesh_context, violations, body = build_briefing(orbit_fixture, lynkmesh_fixture)
    comment_path = LocalMRCommentAdapter(output).post_comment(body)
    run_log = base_run_log(
        mode="mock",
        orbit_context=orbit_context,
        lynkmesh_context=lynkmesh_context,
        violations=violations,
        comment_output_path=str(comment_path),
    )
    run_log["comment_posted"] = True
    return write_run_log(run_log)


def run_gitlab_api(
    *,
    orbit_fixture: Path,
    lynkmesh_fixture: Path,
    output: Path,
    project_id: str | None,
    merge_request_iid: str | None,
    base_url: str | None,
    dry_run: bool,
) -> dict[str, Any]:
    orbit_context, lynkmesh_context, violations, body = build_briefing(orbit_fixture, lynkmesh_fixture)

    # Always write the local artifact too. It is useful for screenshots,
    # debugging, and Devpost evidence even when the GitLab API post succeeds.
    comment_path = LocalMRCommentAdapter(output).post_comment(body)

    adapter = GitLabMRCommentAdapter.from_env(
        project_id=project_id,
        merge_request_iid=merge_request_iid,
        base_url=base_url,
        dry_run=dry_run,
    )
    post_result = adapter.post_comment(body)

    run_log = base_run_log(
        mode="gitlab_api",
        orbit_context=orbit_context,
        lynkmesh_context=lynkmesh_context,
        violations=violations,
        comment_output_path=str(comment_path),
    )
    run_log["gitlab"] = post_result.as_log()
    run_log["comment_posted"] = post_result.posted
    run_log["dry_run"] = post_result.dry_run
    return write_run_log(run_log)


def main() -> None:
    parser = argparse.ArgumentParser(description="Orbit Guardrail Agent")
    parser.add_argument("--mode", choices=["mock", "gitlab_api"], default="mock")
    parser.add_argument("--orbit-fixture", default=str(DEFAULT_ORBIT_FIXTURE))
    parser.add_argument("--lynkmesh-fixture", default=str(DEFAULT_LYNKMESH_FIXTURE))
    parser.add_argument("--out", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--project-id", default=None, help="GitLab numeric project ID or URL-encoded path source.")
    parser.add_argument("--mr-iid", default=None, help="GitLab merge request IID, not the global MR ID.")
    parser.add_argument("--gitlab-base-url", default=None, help="Defaults to GITLAB_BASE_URL or https://gitlab.com.")
    parser.add_argument("--dry-run", action="store_true", help="Generate log and endpoint without posting to GitLab.")
    args = parser.parse_args()

    if args.mode == "mock":
        run_log = run_mock(Path(args.orbit_fixture), Path(args.lynkmesh_fixture), Path(args.out))
    else:
        run_log = run_gitlab_api(
            orbit_fixture=Path(args.orbit_fixture),
            lynkmesh_fixture=Path(args.lynkmesh_fixture),
            output=Path(args.out),
            project_id=args.project_id,
            merge_request_iid=args.mr_iid,
            base_url=args.gitlab_base_url,
            dry_run=args.dry_run,
        )

    print(json.dumps(run_log, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
