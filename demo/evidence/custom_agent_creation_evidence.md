# Custom Agent Creation Evidence

## Status

Orbit Guardrail Agent was created as a custom GitLab Duo agent in the provisioned GitLab Transcend hackathon workspace.

This evidence records custom-agent creation and manual review behavior. It does not claim completed AI Catalog publication, automatic trigger execution, or live GitLab Orbit API integration.

## GitLab Workspace

* Platform: GitLab
* Hackathon workspace: GitLab AI Hackathon / Transcend
* Project path: `gitlab-ai-hackathon/transcend/39119538`
* Merge Request: `!1`
* MR title: `Add Orbit Guardrail Agent prototype`

## Custom Agent

* Agent name: `Orbit Guardrail Agent`
* Visibility: `Private`
* Location: `AI -> Agents`
* Creation path: `AI -> Agents -> New agent`

## Agent Purpose

Orbit Guardrail Agent is an architecture-aware merge request review agent for GitLab.

It helps reviewers understand whether a merge request violates expected layered architecture boundaries, especially the rule:

```text
Controller -> Service -> Model is expected.
Controller -> Model is a potential service-layer bypass.
```

The agent frames LynkMesh as context enrichment behind the GitLab workflow, not as a replacement for GitLab Orbit.

## Custom Agent Review Test

The custom agent was tested against GitLab MR `!1`.

The agent correctly identified:

* rule: `layering.controller_to_model_bypass`
* expected flow: `Controller -> Service -> Model`
* detected bad flow: `Controller -> Model`
* violated edge: `InvoiceController::store -> InvoiceModel::create`
* real GitLab MR note ID: `3450765751`
* live GitLab MR posting evidence: `demo/evidence/gitlab_real_mr_run_redacted.md`
* dry-run/local evidence: `demo/evidence/demo_run_log.redacted.json`

## What Is Proven

* A custom GitLab Duo agent can be created in the hackathon workspace.
* The agent can review the repository and MR evidence.
* The agent can explain the architecture guardrail.
* The agent can distinguish dry-run evidence from live GitLab MR posting evidence after correction.
* The Python prototype has posted a real guardrail briefing comment to GitLab MR `!1`.

## What Remains Pending

* AI Catalog publication.
* Automatic trigger execution.
* GitLab Duo workflow hook wiring.
* Live GitLab Orbit context ingestion.
* Live LynkMesh graph query integration.
* CI/CD enforcement.

## Evidence Screenshots

* `demo/screenshots/gitlab_custom_agent_created.png`

## No-Overclaiming Note

This stage proves custom agent creation and manual custom-agent review behavior.

It does not prove that the agent has been published to the AI Catalog, automatically triggered by GitLab events, or connected to a live GitLab Orbit graph API.
