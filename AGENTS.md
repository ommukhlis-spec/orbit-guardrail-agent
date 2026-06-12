# AGENTS.md — Orbit Guardrail Agent

## Project role

This repository contains **Orbit Guardrail Agent powered by LynkMesh**, a GitLab Transcend Showcase Track prototype.

The goal is to demonstrate an architecture-aware Merge Request guardrail workflow for GitLab Duo and GitLab Orbit.

## Core framing

- GitLab Orbit is the GitLab-native project context / knowledge graph layer.
- GitLab Duo Agent Platform is the workflow and agent execution surface.
- LynkMesh is a deterministic context enrichment concept used here to provide graph-backed dependency, impact, and blast-radius context.
- LynkMesh does not replace GitLab Orbit.
- The current prototype uses mock Orbit-style and LynkMesh-style fixtures for deterministic demonstration, plus a real GitLab MR comment action through GitLab API.

## Implemented today

- Mock Orbit-style context adapter.
- Mock LynkMesh-style impact adapter.
- Guardrail engine for `layering.controller_to_model_bypass`.
- MR briefing renderer.
- GitLab API dry-run and real MR comment mode.
- Demo before/after scenario for Controller -> Model service-layer bypass.
- Real GitLab MR evidence pack.

## Primary rule

A Controller should not directly access a Model when a Service layer exists.

Expected architecture:

```text
Controller -> Service -> Model
```

Detected violation:

```text
Controller -> Model
```

## What to do when reviewing this project

When asked to analyze the Merge Request or repository:

1. Inspect the demo scenario under `demo/invoice_app_before/` and `demo/invoice_app_after_bad_mr/`.
2. Inspect `demo/sample_mr_comment.md` and `demo/evidence/gitlab_real_mr_run_redacted.md`.
3. Explain how the workflow detects the Controller -> Model bypass.
4. Mention that repo-wide blast radius includes:
   - `InvoiceService::createInvoice`
   - `BillingEngine::syncInvoice`
   - `ReportExportService::monthlyInvoiceSummary`
5. Keep claims conservative.

## Do not claim

- Do not claim this is a complete production code reviewer.
- Do not claim LynkMesh replaces GitLab Orbit.
- Do not claim real GitLab Orbit/Duo custom agent integration is complete until evidence exists.
- Do not claim AI automatically fixes or merges code.

## Safe summary

Orbit Guardrail Agent demonstrates how GitLab Duo workflows can be enriched with architecture-aware context to generate reviewer-ready MR guardrail briefings.
