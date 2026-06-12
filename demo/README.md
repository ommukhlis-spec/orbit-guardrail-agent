# Demo Assets

This folder contains the demo scenario for **Orbit Guardrail Agent powered by LynkMesh**.

The demo intentionally compares two small PHP application snapshots:

- `invoice_app_before/` — safe layered architecture: `Controller -> Service -> Model`.
- `invoice_app_after_bad_mr/` — bad MR scenario: `Controller -> Model`.

The agent should detect the service-layer bypass and generate a reviewer-ready merge request briefing with architecture violation, blast radius, suggested tests, and context evidence.

## Run the local mock demo

```bash
python -m app.main --mode mock --out demo/sample_mr_comment.md
```

## Run the GitLab API dry-run

```bash
python -m app.main --mode gitlab_api --project-id demo/group --mr-iid 12 --dry-run
```

The dry-run prints the GitLab MR notes endpoint without posting a real comment.
