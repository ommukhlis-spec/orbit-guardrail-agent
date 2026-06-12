# Stage 5 — GitLab Real MR Demo Prep

Status: preparation stage. This document prepares the repository for a real GitLab Merge Request demonstration while the GitLab Transcend dedicated project is still pending approval/provisioning.

## Goal

Prepare a repeatable demo path where Orbit Guardrail Agent can post its architecture-aware briefing to a real GitLab Merge Request.

This stage does **not** claim final GitLab Orbit / Duo Agent Platform integration yet. It prepares the GitLab MR workflow that will later be connected to the provisioned hackathon project.

## Demo flow

```text
Clean demo app
  Controller -> Service -> Model
        ↓
Bad MR branch
  Controller -> Model
        ↓
Orbit Guardrail Agent
  detects service-layer bypass
        ↓
GitLab MR comment
  violation + blast radius + suggested tests + context evidence
```

## Prerequisites

- A GitLab account.
- A GitLab project for the demo, preferably the dedicated hackathon project once provisioned.
- A Merge Request containing the intentional bad change from `demo/invoice_app_after_bad_mr`.
- A GitLab access token with permission to create MR notes/comments.

Do not commit tokens, `.env` files, screenshots containing secrets, or private GitLab project credentials.

## Dry-run command

Use dry-run first. This validates endpoint generation without posting to GitLab.

```powershell
python -m app.main --mode gitlab_api --project-id "GROUP/PROJECT" --mr-iid 1 --dry-run
```

Expected output includes:

```json
{
  "mode": "gitlab_api",
  "dry_run": true,
  "gitlab": {
    "posted": false,
    "endpoint": "https://gitlab.com/api/v4/projects/GROUP%2FPROJECT/merge_requests/1/notes"
  }
}
```

## Live comment command

After validating the target MR and token locally:

```powershell
set GITLAB_TOKEN=glpat_REDACTED
python -m app.main --mode gitlab_api --project-id "GROUP/PROJECT" --mr-iid 1
```

Expected result:

- `gitlab.posted: true`
- `gitlab.note_id` is present
- `gitlab.web_url` is present if returned by GitLab
- The MR contains the rendered Orbit Guardrail Briefing comment

## Evidence to capture

For the final hackathon demo/evidence package, capture:

1. GitLab MR link.
2. Screenshot of the changed `InvoiceController.php` file.
3. Screenshot of the agent-generated MR comment.
4. Redacted run log from `app/logs/`.
5. Link to `demo/sample_mr_comment.md`.
6. Link to `demo/evidence/context_evidence_matrix.md`.

## Safe claims

Safe:

- The local guardrail engine detects a deterministic Controller -> Model bypass.
- The GitLab API mode can post the generated briefing to a GitLab MR.
- The repository includes a real demo scenario and evidence templates.
- GitLab Orbit / Duo integration is prepared as the next step after provisioning.

Do not claim yet:

- Final GitLab Orbit integration is complete.
- The agent is published to the AI Catalog.
- The workflow is production-ready.
- The agent is a complete code reviewer.
