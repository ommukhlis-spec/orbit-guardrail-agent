# Orbit Guardrail Agent powered by LynkMesh

**Repo-Wide Architecture Awareness for GitLab Duo Flows**

Orbit Guardrail Agent is a hackathon MVP that demonstrates how a GitLab Duo workflow can review Merge Requests with architecture-aware context, not only local diff text.

The MVP focuses on one deterministic guardrail:

> Controller should not directly access Model when a Service layer exists.

The agent reads Merge Request context, uses GitLab Orbit-style project context, enriches it with LynkMesh-style graph-backed impact context, detects architecture violations, and renders a reviewer-ready MR briefing.

## Status

Early hackathon prototype. The current implementation starts with mock fixtures so the guardrail logic is deterministic and testable. The adapter boundaries are designed so mock context can later be replaced by GitLab Orbit API/CLI/skill interface and GitLab MR integration.

## Positioning

- GitLab Orbit = GitLab-native project knowledge graph / context substrate.
- GitLab Duo Agent Platform = workflow execution surface.
- LynkMesh = deterministic context enrichment engine for repo-wide dependency and blast-radius context.
- Orbit Guardrail Agent = the submitted hackathon agent/workflow.

LynkMesh does **not** replace GitLab Orbit. It enriches agent workflows with graph-backed context and evidence.

## Quickstart

```bash
python -m pytest -q
python -m app.main --mode mock --out demo/sample_mr_comment.md
```

Windows PowerShell:

```powershell
python -m pytest -q
python -m app.main --mode mock --out demo\sample_mr_comment.md
```

Expected outputs:

- `demo/sample_mr_comment.md`
- `app/logs/run_*.json`

## Demo Flow

```text
Mock MR fixture
→ Mock Orbit context
→ Mock LynkMesh impact context
→ Guardrail Engine
→ MR briefing renderer
→ sample MR comment + run log
```

## What the MVP Shows

- Architecture guardrail detection
- Expected vs detected architecture flow
- Repo-wide blast radius
- Suggested tests
- Reviewer checklist
- Context evidence IDs

## Safe Claims

This prototype detects one narrow architecture rule. It does not perform full autonomous review, does not automatically fix code, and does not prove runtime behavior.
