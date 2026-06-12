# Stage 9 — Orbit/Duo Agentic Workflow Exploration

## Purpose

Stage 9 explores how the prototype should be represented inside the GitLab Duo Agent Platform and AI Catalog.

The repository already proves a real GitLab workflow action: the agent generated and posted an architecture guardrail briefing to Merge Request `!1` in the provisioned GitLab Transcend workspace.

Stage 9 focuses on the remaining Showcase Track requirement:

- interact with GitLab Orbit / Duo Agent Platform,
- document the agent/flow/skill packaging approach,
- prepare AI Catalog submission notes,
- capture evidence conservatively.

## Current status

Implemented:

- GitHub repository is public.
- GitLab provisioned project exists.
- Branch `orbit-guardrail-agent` is pushed to GitLab.
- Merge Request `!1` exists.
- Real GitLab MR comment was posted by the agent.
- Evidence screenshots and redacted evidence markdown are committed.

Pending:

- Real GitLab Orbit/Duo custom agent or flow packaging.
- AI Catalog publication.
- Final Devpost video.

## Recommended exploration path

### Step 1 — Confirm Duo and Orbit are enabled

In the GitLab provisioned project or namespace:

- Confirm GitLab Duo is enabled.
- Confirm `Use Orbit in GitLab Duo` is enabled.
- Confirm Agentic Chat is available.

Evidence to capture:

- screenshot of Duo/Orbit enabled,
- screenshot of MR `!1` with Duo panel visible,
- screenshot of agent comment.

### Step 2 — Ask Duo to inspect the MR

Use the prompts in `demo/orbit_duo_prompts.md`.

The goal is not to force Duo to reproduce the whole agent. The goal is to show that the project can be explained and navigated with Orbit/Duo context.

### Step 3 — Identify AI Catalog path

Open GitLab AI Catalog in the GitLab UI and inspect whether this workspace supports:

- creating a custom agent,
- creating a custom flow,
- adding an external agent,
- publishing/sharing to AI Catalog.

Capture a short note in:

```text
 demo/evidence/orbit_duo_exploration_log.md
```

### Step 4 — Decide packaging approach

Preferred final packaging:

```text
Custom flow or external agent entry:
MR Architecture Guardrail Briefing
```

Minimum viable final artifact:

- a GitLab MR workflow action already demonstrated through GitLab API,
- AGENTS.md project instructions for Duo/flow context,
- documentation describing how Orbit context and LynkMesh enrichment are used,
- AI Catalog submission notes or publication link if available.

## Go / No-Go rule

GO if at least one of these becomes available:

- custom agent creation works,
- custom flow creation works,
- external agent entry can be added to AI Catalog,
- GitLab provides a hackathon-specific AI Catalog submission path.

NO-GO for claiming full integration if:

- only mock fixtures are used,
- no AI Catalog or Duo/Orbit packaging artifact exists,
- Duo is only used as a generic chatbot with no project/MR context.

## Safe public wording

Use:

> The prototype has posted a real architecture guardrail briefing to a GitLab Merge Request. The next step is packaging this workflow as a GitLab Duo/Orbit agent, flow, or skill and publishing it to the AI Catalog.

Avoid:

> The agent is fully integrated with GitLab Orbit and AI Catalog.

Use the latter only after evidence exists.
