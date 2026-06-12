# GitLab Real MR Evidence — Redacted

## Status

A real GitLab Merge Request comment was posted successfully by Orbit Guardrail Agent in the GitLab Transcend provisioned workspace.

## GitLab Workspace

* Platform: GitLab
* Hackathon workspace: GitLab AI Hackathon / Transcend
* Project path: `gitlab-ai-hackathon/transcend/39119538`
* Merge Request: `!1`
* MR title: `Add Orbit Guardrail Agent prototype`

## Agent Action

Command mode:

```text
gitlab_api
```

Action performed:

```text
Post reviewer-ready architecture guardrail briefing to a real GitLab Merge Request.
```

Result:

```text
posted: true
```

## Run Metadata

* run_id: `8fc18aef-4b98-43c3-8365-1e3bf6694235`
* note_id: `3450765751`
* mode: `gitlab_api`
* comment_posted: `true`
* dry_run: `false`
* context_pack_id: `sha256:demo-context-pack`
* rule evaluated: `layering.controller_to_model_bypass`

## Guardrail Detected

Rule:

```text
Controller should not directly access Model when a Service layer exists.
```

Expected architecture:

```text
Controller -> Service -> Model
```

Detected architecture:

```text
Controller -> Model
```

## Blast Radius

The generated MR briefing included repo-wide impact context for:

* `InvoiceService::createInvoice`
* `BillingEngine::syncInvoice`
* `ReportExportService::monthlyInvoiceSummary`

## Evidence Screenshots

* `demo/screenshots/gitlab_mr_overview_summary.png`
* `demo/screenshots/gitlab_mr_status_and_pending_integration.png`
* `demo/screenshots/gitlab_mr_guardrail_comment_full.png`

## Important Scope Note

This evidence proves that the prototype can generate and post an architecture guardrail briefing to a real GitLab Merge Request.

The current implementation uses mock Orbit-style and LynkMesh-style context fixtures for deterministic demonstration. Real GitLab Orbit/Duo integration and AI Catalog publishing remain pending next steps.
