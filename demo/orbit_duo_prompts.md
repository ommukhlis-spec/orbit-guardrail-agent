# Orbit/Duo Exploration Prompts

Use these prompts in GitLab Duo Agentic Chat inside the provisioned project.

## Prompt 1 — Understand the MR

```text
Use the project context and this merge request to summarize what Orbit Guardrail Agent does. Focus on the architecture guardrail workflow, the demo before/after scenario, and the real MR comment evidence. Do not overclaim production readiness.
```

## Prompt 2 — Inspect the architecture violation

```text
Inspect the demo files and explain the architecture rule demonstrated by this project. Compare the expected flow Controller -> Service -> Model with the bad MR flow Controller -> Model. Identify which files represent the before and after states.
```

## Prompt 3 — Reviewer briefing

```text
Generate a concise reviewer briefing for this MR. Include the guardrail violation, expected architecture, detected architecture, blast radius, suggested tests, and current limitations.
```

## Prompt 4 — AI Catalog packaging advice

```text
Based on this repository, propose the best GitLab Duo Agent Platform packaging approach: custom agent, custom flow, external agent, or skill. Explain what should be published to the AI Catalog and what evidence is still missing.
```

## Prompt 5 — Conservative Devpost update

```text
Draft a conservative Devpost update paragraph for Orbit Guardrail Agent. Mention that the prototype posted a real GitLab MR comment and that real Orbit/Duo AI Catalog packaging is the next step. Do not claim completed AI Catalog publication yet.
```
