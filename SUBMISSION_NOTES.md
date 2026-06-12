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
