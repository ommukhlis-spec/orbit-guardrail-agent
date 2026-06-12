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
