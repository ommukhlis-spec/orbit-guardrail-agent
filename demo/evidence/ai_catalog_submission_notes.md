# AI Catalog Submission Notes — Draft

## Candidate name

Orbit Guardrail Agent powered by LynkMesh

## Candidate type

Preferred:

```text
Custom flow or external agent
```

Fallback:

```text
Skill-style workflow documentation with MR comment action evidence
```

## Short description

Architecture-aware Merge Request guardrail workflow that detects service-layer bypasses and posts reviewer-ready impact briefings to GitLab Merge Requests.

## Problem solved

AI code review can miss repo-wide architecture impact when it only reviews the local diff. Orbit Guardrail Agent focuses on a narrow but practical reviewer workflow: detecting when a Controller bypasses the Service layer and directly accesses a Model.

## Workflow

```text
Merge Request context
-> Orbit-style project context
-> LynkMesh-style dependency and blast-radius context
-> guardrail engine
-> reviewer-ready MR briefing
-> GitLab MR comment
```

## Evidence

- Real GitLab MR comment posted to `!1`.
- Redacted evidence: `demo/evidence/gitlab_real_mr_run_redacted.md`.
- Screenshots: `demo/screenshots/`.
- GitHub repository: `https://github.com/ommukhlis-spec/orbit-guardrail-agent`.

## Safe limitation note

Current implementation proves the guardrail workflow and real GitLab MR action. The Orbit/Duo/AI Catalog packaging step is being explored during Stage 9.
