# Stage 4 — Evidence Artifacts and Demo Polish

Stage 4 prepares the project for external review while GitLab Showcase provisioning is still pending.

## Purpose

The goal is to make the repository understandable to judges and reviewers without requiring access to private logs or live GitLab credentials.

## Added assets

- `demo/evidence/README.md`
- `demo/evidence/demo_run_log.redacted.json`
- `demo/evidence/context_evidence_matrix.md`
- `demo/evidence/submission_checklist.md`
- `demo/video_shot_list.md`

## What this proves

The current repository proves the local deterministic workflow:

```text
MR fixture
-> Orbit-style context fixture
-> LynkMesh-style impact context fixture
-> guardrail engine
-> reviewer-ready MR briefing
-> run evidence
```

It also proves that the GitLab MR comment endpoint can be constructed safely in dry-run mode.

## What remains pending

Final hackathon compliance still requires:

- a provisioned GitLab project,
- GitLab Orbit API/CLI/skill interface use,
- GitLab Duo Agent Platform wrapper,
- AI Catalog publication,
- a final 3-minute demo video.

## Safe external framing

Use this wording:

> This is an early hackathon prototype. The current implementation demonstrates deterministic local guardrail analysis and GitLab API dry-run mode. The final Showcase integration will connect the adapter boundary to GitLab Orbit/Duo after the hackathon project is provisioned.

Avoid claiming full GitLab Orbit/Duo integration until it is actually working.
