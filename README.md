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

## GitLab API comment mode

The first prototype mode writes the generated guardrail briefing to a local markdown file. The next integration step is `gitlab_api` mode, which posts the same reviewer-ready briefing as a merge request note.

This mode still uses the mock Orbit and LynkMesh fixtures for context. Its purpose is to prove the workflow action surface: generate a guardrail briefing and post it to a real GitLab Merge Request.

Dry run, no token required:

```bash
python -m app.main --mode gitlab_api --project-id <PROJECT_ID_OR_PATH> --mr-iid <MR_IID> --dry-run
```

Real post:

```bash
set GITLAB_TOKEN=<your_token>
python -m app.main --mode gitlab_api --project-id <PROJECT_ID_OR_PATH> --mr-iid <MR_IID>
```

Optional environment variables:

```bash
GITLAB_BASE_URL=https://gitlab.com
GITLAB_PROJECT_ID=<PROJECT_ID_OR_PATH>
GITLAB_MR_IID=<MR_IID>
GITLAB_TOKEN=<token>
```

Notes:

- `MR_IID` means the merge request IID shown inside a project, not the global merge request ID.
- `PROJECT_ID_OR_PATH` may be a numeric project ID or a namespace path such as `group/project`.
- This posts a top-level merge request note through the GitLab API. Line-level discussions can be added later if needed.
- Do not commit tokens, `.env` files, private project IDs, or screenshots containing secrets.

<!-- STAGE3_DEMO_SCENARIO_START -->
## Demo Scenario: Intentional Architecture Violation

This repository includes a small demo application under `demo/` to make the guardrail workflow easy to understand.

The demo compares:

- `demo/invoice_app_before/` — expected layered flow: `Controller -> Service -> Model`.
- `demo/invoice_app_after_bad_mr/` — intentionally bad MR flow: `Controller -> Model`.

The hero workflow is:

```text
small MR diff
-> Orbit-style changed-file context
-> LynkMesh-style dependency and blast-radius context
-> guardrail engine
-> reviewer-ready MR briefing
```

Run the local mock demo:

```bash
python -m app.main --mode mock --out demo/sample_mr_comment.md
```

Run GitLab API mode without posting a real comment:

```bash
python -m app.main --mode gitlab_api --project-id demo/group --mr-iid 12 --dry-run
```

The final hackathon integration should replace mock Orbit context with GitLab Orbit API, CLI, or skill-interface context and run inside the GitLab Duo/AI Catalog workflow.
<!-- STAGE3_DEMO_SCENARIO_END -->

<!-- STAGE4_EVIDENCE_POLISH_START -->
## Stage 4 Evidence and Demo Polish

The repository now includes a public-safe demo evidence pack under `demo/evidence/`.

Useful links:

- `demo/mr_diff.md` — tiny bad MR used in the demo.
- `demo/invoice_app_before/` — expected layered architecture.
- `demo/invoice_app_after_bad_mr/` — intentional service-layer bypass.
- `demo/sample_mr_comment.md` — generated reviewer-ready briefing.
- `demo/evidence/demo_run_log.redacted.json` — redacted sample run log.
- `demo/evidence/context_evidence_matrix.md` — maps claims to evidence artifacts.
- `demo/video_shot_list.md` — 3-minute demo recording plan.

Current safe status: local mock workflow and GitLab API dry-run mode are implemented. GitLab Orbit/Duo/AI Catalog integration remains pending until the hackathon-provisioned project is available.
<!-- STAGE4_EVIDENCE_POLISH_END -->

## GitLab real MR demo prep

Stage 5 prepares the project for a real GitLab Merge Request demonstration. The repository now includes a checklist, evidence template, and helper script for creating a demo MR that intentionally bypasses the service layer.

Start here:

- [Stage 5 GitLab Real MR Demo Prep](docs/stage5_gitlab_real_mr_prep.md)
- [GitLab Real MR Demo Checklist](demo/gitlab_real_mr_checklist.md)
- [GitLab Real MR Evidence Template](demo/evidence/gitlab_real_mr_evidence_template.md)

This stage prepares the GitLab MR workflow. Final GitLab Orbit / Duo Agent Platform integration remains pending until the hackathon project is provisioned.

<!-- STAGE9_ORBIT_DUO_EXPLORATION_START -->
## Stage 9 — Orbit/Duo exploration

The prototype has now demonstrated a real GitLab workflow action by posting an architecture guardrail briefing to Merge Request `!1` in the provisioned GitLab Transcend workspace.

Stage 9 explores the remaining Showcase packaging path: representing the workflow as a GitLab Duo/Orbit agent, flow, skill, or external agent entry and preparing AI Catalog submission notes.

New Stage 9 assets:

- `AGENTS.md` — project instructions for GitLab Duo / agentic workflow context.
- `docs/stage9_orbit_duo_agentic_workflow.md` — exploration plan and safe claims.
- `demo/orbit_duo_prompts.md` — prompts for Duo/Orbit exploration.
- `demo/evidence/orbit_duo_exploration_log.md` — evidence log template.
- `demo/evidence/ai_catalog_submission_notes.md` — draft AI Catalog packaging notes.

Current limitation: real GitLab Orbit/Duo custom agent or AI Catalog publication remains pending until verified with evidence.
<!-- STAGE9_ORBIT_DUO_EXPLORATION_END -->

## Current Evidence Status

Orbit Guardrail Agent currently demonstrates:

- a deterministic architecture guardrail engine for merge request review,
- a real GitLab MR comment posted through the GitLab Notes API,
- a custom GitLab Duo agent created in the provisioned hackathon workspace,
- GitLab Duo/Orbit-assisted repository understanding and evidence review,
- AI Catalog visibility as a private custom agent in the hackathon workspace.

The current implementation intentionally avoids overclaiming. The Orbit-style and LynkMesh-style adapters use deterministic local fixtures for the demo scenario. Live GitLab Orbit API ingestion, automatic trigger execution, public AI Catalog publication, and production CI/CD enforcement remain pending.

Safe summary:

`Orbit Guardrail Agent is a GitLab MR guardrail prototype with real MR comment evidence, custom Duo agent evidence, and private AI Catalog visibility in the provisioned hackathon workspace.`
