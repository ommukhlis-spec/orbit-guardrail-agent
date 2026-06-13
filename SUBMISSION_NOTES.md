# Submission Notes

## Project Name

Orbit Guardrail Agent powered by LynkMesh

## Subtitle

Repo-Wide Architecture Awareness for GitLab Duo Flows

## Short Description

Orbit Guardrail Agent reviews GitLab Merge Requests with architecture-aware context. It uses GitLab Orbit-style project context and LynkMesh-style dependency context to detect guardrail violations, explain blast radius, suggest tests, and generate reviewer-ready MR briefings.

## Track

Showcase Track

## What to Avoid Claiming

- Do not claim LynkMesh replaces GitLab Orbit.
- Do not claim the agent is a complete code reviewer.
- Do not claim the agent automatically fixes code.
- Do not claim mock mode alone satisfies the final hackathon integration.

## Safe Framing

The prototype demonstrates a deterministic architecture guardrail workflow and is designed to integrate with GitLab Orbit/Duo once the hackathon project surface is available.

## Integration status

Current implemented modes:

- `mock`: deterministic local flow that renders the MR guardrail briefing to markdown.
- `gitlab_api`: posts the generated briefing as a top-level GitLab Merge Request note. This proves the workflow action surface while Orbit/Duo provisioning is pending.

Still pending for final Showcase eligibility:

- real GitLab Orbit API/CLI/skill interface integration,
- Duo Agent Platform wrapper or flow,
- AI Catalog publication.

<!-- STAGE3_DEMO_SCENARIO_START -->
## Stage 3 Demo Scenario

A demo repository snapshot has been added under `demo/`.

The demo shows a small bad merge request where `InvoiceController` bypasses `InvoiceService` and calls `InvoiceModel` directly.

This is the main visual scenario for the hackathon demo:

```text
Before: InvoiceController -> InvoiceService -> InvoiceModel
After:  InvoiceController -> InvoiceModel
```

Why it matters:

- The local diff is small.
- The architecture impact is repo-wide.
- LynkMesh-style context provides blast-radius evidence.
- The agent produces a reviewer-ready MR briefing instead of generic code-review text.

Current status:

- Mock flow works locally.
- GitLab API dry-run mode is available.
- Real GitLab posting should be tested after a dedicated/provisioned GitLab project or demo MR is available.
- Orbit/Duo/AI Catalog integration is still pending hackathon provisioning.
<!-- STAGE3_DEMO_SCENARIO_END -->

<!-- STAGE4_EVIDENCE_STATUS_START -->
## Stage 4 Evidence Status

Stage 4 adds public-safe evidence and demo-polish assets.

Added:

- `demo/evidence/demo_run_log.redacted.json`
- `demo/evidence/context_evidence_matrix.md`
- `demo/evidence/submission_checklist.md`
- `demo/video_shot_list.md`
- `docs/stage4_evidence_artifacts.md`

Use these artifacts to support the Devpost project page and final demo video.

Safe current claim:

> The project has a deterministic local MVP, a clear before/after demo scenario, tests, generated MR briefing output, redacted sample run evidence, and GitLab API dry-run mode.

Pending claim:

> Full GitLab Orbit/Duo/AI Catalog integration is pending the dedicated GitLab project and Showcase provisioning.
<!-- STAGE4_EVIDENCE_STATUS_END -->

## Stage 5 update — GitLab real MR prep

The repository now includes a repeatable path for rehearsing a real GitLab Merge Request demonstration:

- demo project setup helper: `scripts/prepare_real_mr_demo.ps1`
- real MR checklist: `demo/gitlab_real_mr_checklist.md`
- evidence template: `demo/evidence/gitlab_real_mr_evidence_template.md`
- preparation doc: `docs/stage5_gitlab_real_mr_prep.md`

Current status remains conservative:

- Local mock mode works.
- GitLab API dry-run mode works.
- Real GitLab MR comment mode is prepared.
- GitLab Orbit / Duo / AI Catalog integration is still pending hackathon provisioning.

<!-- STAGE9_SUBMISSION_NOTES_START -->
## Stage 9 — Orbit/Duo and AI Catalog readiness

Current proof:

- real GitLab MR comment posted to `!1`,
- redacted evidence committed,
- screenshots committed,
- GitHub and GitLab branches updated.

Next proof needed for final Showcase readiness:

- verify the best AI Catalog packaging path,
- publish or register the agent/flow/skill if the UI supports it,
- capture the publication link or submission evidence,
- avoid claiming completed Orbit/Duo custom integration until verified.

Safe Devpost wording:

> Orbit Guardrail Agent has demonstrated a real GitLab MR workflow action by posting an architecture guardrail briefing to MR `!1`. The next step is packaging this workflow as a GitLab Duo/Orbit agent, flow, skill, or external agent entry and publishing it to the AI Catalog.
<!-- STAGE9_SUBMISSION_NOTES_END -->

## Final Submission Evidence Summary

The project has accumulated the following evidence:

- Real GitLab MR comment evidence:
  - `demo/evidence/gitlab_real_mr_run_redacted.md`
  - `demo/screenshots/gitlab_mr_guardrail_comment_full.png`

- Custom GitLab Duo agent evidence:
  - `demo/evidence/custom_agent_creation_evidence.md`
  - `demo/evidence/orbit_duo_exploration_log.md`
  - `demo/screenshots/gitlab_custom_agent_created.png`

- AI Catalog feasibility evidence:
  - `demo/evidence/ai_catalog_feasibility_evidence.md`
  - `demo/screenshots/gitlab_ai_catalog_orbit_guardrail_agent_private.png`

- Architecture/context evidence:
  - `demo/evidence/context_evidence_matrix.md`
  - `demo/evidence/demo_run_log.redacted.json`

Submission-safe claim:

`Orbit Guardrail Agent posts a real architecture guardrail briefing to a GitLab MR, has a custom GitLab Duo agent created in the hackathon workspace, and appears in the AI Catalog tab as a private custom agent.`

Do not claim:

- public AI Catalog publication,
- automatic MR trigger execution,
- live GitLab Orbit API ingestion,
- live LynkMesh graph query integration,
- production-ready CI enforcement.
