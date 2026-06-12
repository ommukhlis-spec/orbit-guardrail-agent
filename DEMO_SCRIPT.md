# 3-Minute Demo Script

## 0:00–0:20 — Problem

AI code review often sees changed files, but misses repo-wide architectural impact.

## 0:20–0:45 — Setup

Show a Merge Request changing `InvoiceController.php`.

Explain expected architecture:

```text
Controller → Service → Model
```

## 0:45–1:20 — Run Agent

Run:

```bash
python -m app.main --mode mock --out demo/sample_mr_comment.md
```

## 1:20–2:20 — Show MR Briefing

Highlight:

- Direct Model access violation
- Expected vs detected flow
- Blast radius: InvoiceService, BillingEngine, ReportExportService
- Suggested tests
- Reviewer checklist

## 2:20–2:45 — Show Evidence Log

Show `app/logs/run_*.json` with context IDs and rules evaluated.

## 2:45–3:00 — Close

Orbit Guardrail Agent makes GitLab Duo flows architecture-aware by enriching Orbit context with LynkMesh graph-backed impact context.

<!-- STAGE3_DEMO_FLOW_START -->
## Stage 3 Demo Flow

Use this script once the demo repository and mock workflow are committed.

1. Open `demo/mr_diff.md` and show the tiny code change.
2. Open `demo/invoice_app_before/app/Http/Controllers/InvoiceController.php`.
3. Show the expected flow: `Controller -> Service -> Model`.
4. Open `demo/invoice_app_after_bad_mr/app/Http/Controllers/InvoiceController.php`.
5. Show the bad flow: `Controller -> Model`.
6. Run:

```bash
python -m app.main --mode mock --out demo/sample_mr_comment.md
```

7. Open `demo/sample_mr_comment.md` and highlight:
   - architecture violation,
   - expected vs detected flow,
   - blast radius,
   - suggested tests,
   - reviewer checklist,
   - context evidence.
8. Run GitLab API dry-run:

```bash
python -m app.main --mode gitlab_api --project-id demo/group --mr-iid 12 --dry-run
```

9. Show the generated GitLab MR notes endpoint.
10. Explain that final hackathon mode replaces the mock Orbit adapter with GitLab Orbit/Duo integration after provisioning.
<!-- STAGE3_DEMO_FLOW_END -->

<!-- STAGE4_RECORDING_PLAN_START -->
## Stage 4 Recording Plan

Use `demo/video_shot_list.md` as the final recording plan for the 3-minute Devpost video.

Recommended recording order:

1. Show `demo/mr_diff.md`.
2. Show expected architecture under `demo/invoice_app_before/`.
3. Show bad MR under `demo/invoice_app_after_bad_mr/`.
4. Run mock mode.
5. Open `demo/sample_mr_comment.md`.
6. Show `demo/evidence/demo_run_log.redacted.json`.
7. Run GitLab API dry-run.
8. Close with the Orbit + LynkMesh positioning.

Do not show private tokens, real customer data, browser cookies, or local-only secrets.
<!-- STAGE4_RECORDING_PLAN_END -->
