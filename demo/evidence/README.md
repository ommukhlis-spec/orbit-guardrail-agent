# Demo Evidence Pack

This folder contains public-safe evidence artifacts for the **Orbit Guardrail Agent powered by LynkMesh** hackathon demo.

The artifacts are intentionally small and redacted. They are meant to show the workflow shape without exposing private repositories, tokens, GitLab secrets, or real customer data.

## Files

- `demo_run_log.redacted.json` — sample execution log from the guardrail workflow.
- `context_evidence_matrix.md` — maps each demo claim to the artifact that supports it.
- `submission_checklist.md` — final readiness checklist for Devpost/GitLab submission.

## Safe scope

Current evidence proves that the local mock workflow can:

1. load a merge request fixture,
2. load Orbit-style changed-file context,
3. load LynkMesh-style impact context,
4. detect one architecture guardrail violation,
5. render a reviewer-ready MR briefing,
6. produce a run log,
7. simulate the GitLab MR comment endpoint in dry-run mode.

It does **not** yet prove final GitLab Duo/Orbit/AI Catalog integration. That remains pending until the hackathon-provisioned GitLab project is available.
