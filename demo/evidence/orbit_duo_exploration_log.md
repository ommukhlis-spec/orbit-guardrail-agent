# Orbit/Duo Exploration Log

## Status

Stage 9 captures how GitLab Duo/Orbit understands the Orbit Guardrail Agent repository and what packaging path it suggests for GitLab Duo Agent Platform / AI Catalog.

This is exploration evidence, not a claim of completed AI Catalog publication.

---

## Prompt 1 — Repository Understanding

### Prompt

Explain what this repository does, how the guardrail workflow works, what the before/after demo scenario is, and what evidence exists that the agent posted a real GitLab MR comment.

### Result Summary

GitLab Duo/Orbit correctly identified Orbit Guardrail Agent as a Python prototype for architecture-aware merge request review.

It described the workflow as:

1. loading mock Orbit-style MR context and LynkMesh-style impact context,
2. evaluating deterministic architecture guardrail rules,
3. detecting the `layering.controller_to_model_bypass` rule,
4. rendering a reviewer-ready Markdown briefing,
5. posting that briefing to a GitLab Merge Request through the GitLab Notes API.

It also correctly identified the before/after `invoice-app` demo scenario:

- expected architecture: `Controller -> Service -> Model`
- bad MR architecture: `Controller -> Model`
- violation: `InvoiceController::store` directly calling `InvoiceModel::create`
- bypassed service candidate: `InvoiceService`
- blast radius:
  - `InvoiceService::createInvoice`
  - `BillingEngine::syncInvoice`
  - `ReportExportService::monthlyInvoiceSummary`

Duo/Orbit also recognized that the briefing was posted as a real comment on GitLab MR `!1`, and that this is GitLab API output rather than a screenshot mock.

### Key Takeaway

Duo/Orbit can understand the repository structure, the deterministic guardrail workflow, the before/after architecture scenario, and the real MR comment evidence.

This supports the submission narrative, but does not yet prove live GitLab Orbit API integration, automatic trigger execution, or AI Catalog publication.

---

## Prompt 2 — Packaging Path Toward GitLab Duo Agent Platform

### Prompt

Given this repository and the current GitLab Transcend Showcase Track goal, what is the smallest realistic path to turn this prototype into a GitLab Duo Agent Platform artifact?

Please answer with:

1. Whether this should be packaged as a custom agent, flow, skill, or external agent.
2. What files or metadata should be added to the repository.
3. How this could be published or represented in the AI Catalog.
4. What parts of the current implementation already qualify as workflow automation.
5. What is still missing for Showcase Track compliance.
6. A minimal next-step checklist that avoids overclaiming.

Important context:
- The repository already posts a real MR comment using the GitLab API.
- The current Orbit and LynkMesh adapters use local deterministic fixtures.
- The goal is not to replace GitLab Orbit.
- LynkMesh should be framed as context enrichment behind the GitLab workflow.

### Result Summary

Duo/Orbit suggested that the smallest realistic packaging path is an external-agent-style artifact, because the prototype already has:

- a clear trigger: merge request opened or ready for review,
- a clear action: post a guardrail briefing comment,
- arbitrary Python logic,
- GitLab API integration through the Notes API.

It suggested adding or validating:

- an agent or flow configuration file,
- CI/CD execution metadata,
- project variables or credentials for safe MR comment posting,
- AI Catalog submission notes,
- an end-to-end test using a new MR.

It also identified existing automation evidence:

- the real MR comment on GitLab MR `!1`,
- the working `GitLabMRCommentAdapter`,
- deterministic `GuardrailEngine` evaluation,
- `--dry-run` mode,
- `AGENTS.md` as context for Duo.

### Important Correction

The Duo response claimed that `requirements.txt` was missing, but the repository already has `requirements.txt`.

The response also suggested an external-agent path, but this must be treated as a candidate path until the GitLab hackathon workspace UI confirms exactly what kind of agent can be created and published.

### Key Takeaway

Duo/Orbit reinforced that the project has valid workflow automation evidence, but final Showcase compliance still depends on GitLab Agent Platform / AI Catalog packaging.

The next step is to inspect the GitLab `AI -> Agents -> New agent` form and document whether the workspace supports:

- custom chat agent,
- external agent,
- flow,
- tool/MCP attachment,
- AI Catalog publication.

---

## Current Verified Evidence

- GitLab project has `AI -> Agents`.
- GitLab project has `AI -> Agents -> New agent`.
- A real MR comment was posted to MR `!1`.
- The comment contains the Orbit Guardrail briefing.
- GitLab Duo/Orbit can summarize the repository and identify the prototype caveats.

## Current Unverified / Pending Items

- AI Catalog publication.
- Automatic trigger on merge request ready.
- Live GitLab Orbit API context ingestion.
- External agent CI/CD execution path.
- Public custom agent listing.

## No-Overclaiming Rule

Do not claim the project has been published to the AI Catalog or fully integrated with live GitLab Orbit/Duo until those artifacts exist.

Current honest claim:

Orbit Guardrail Agent is a GitLab MR guardrail prototype with real MR comment posting evidence, Duo/Orbit repository-understanding evidence, and an in-progress path toward GitLab Duo Agent Platform packaging.

## Prompt 3 — Custom Agent MR Review

### Prompt

You are Orbit Guardrail Agent.

Review this merge request using the repository evidence.

Please explain:

1. What architecture guardrail this MR demonstrates.
2. Whether the current prototype has posted a real GitLab MR comment.
3. What the expected architecture flow is.
4. What the detected bad flow is.
5. What blast radius is mentioned in the evidence.
6. What is still pending before this can be claimed as full live Orbit/Duo/AI Catalog integration.

Use AGENTS.md, README, demo evidence, and the MR discussion if available. Avoid overclaiming.

### Result Summary

The custom GitLab Duo agent correctly identified the MR as demonstrating the `layering.controller_to_model_bypass` guardrail. It recognized the expected architecture flow as `Controller -> Service -> Model` and the detected bad flow as `Controller -> Model`.

The agent also identified the real GitLab MR comment evidence, including note ID `3450765751`, and correctly summarized the blast radius:

- `InvoiceService::createInvoice`
- `BillingEngine::syncInvoice`
- `ReportExportService::monthlyInvoiceSummary`

The response remained conservative about pending work, including live Orbit integration, AI Catalog publishing, Duo workflow hooks, and CI/CD enforcement.

### Important Correction

The agent referenced `demo/evidence/demo_run_log.redacted.json` as a dry-run artifact and inferred that the live comment was not captured in the redacted evidence.

That inference is outdated after Stage 8.

The live MR comment evidence is now captured in:

- `demo/evidence/gitlab_real_mr_run_redacted.md`

That file records the live GitLab API run with:

- `run_id: 8fc18aef-4b98-43c3-8365-1e3bf6694235`
- `note_id: 3450765751`
- `posted: true`
- `dry_run: false`

### Key Takeaway

The custom agent can review the MR and explain the guardrail accurately, but its answer shows that the evidence files must clearly distinguish between dry-run evidence and live MR-post evidence.