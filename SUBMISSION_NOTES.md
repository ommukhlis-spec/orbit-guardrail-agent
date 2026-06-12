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
