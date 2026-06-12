# 3-Minute Demo Video Shot List

Goal: show that the agent turns a small local diff into an architecture-aware MR review briefing.

## 0:00–0:20 — Problem

Show `demo/mr_diff.md`.

Narration:

> AI code review often sees the changed file, but misses the architecture behind the repository. This tiny controller change bypasses a service layer and can affect billing and reporting.

## 0:20–0:45 — Expected architecture

Show `demo/invoice_app_before/app/Http/Controllers/InvoiceController.php`.

Highlight:

```text
Controller -> Service -> Model
```

## 0:45–1:10 — Bad MR

Show `demo/invoice_app_after_bad_mr/app/Http/Controllers/InvoiceController.php`.

Highlight:

```text
Controller -> Model
```

## 1:10–1:35 — Run the agent

Run:

```bash
python -m app.main --mode mock --out demo/sample_mr_comment.md
```

Show the JSON run output.

## 1:35–2:20 — Hero artifact

Open `demo/sample_mr_comment.md`.

Highlight:

- architecture guardrail violation,
- expected vs detected flow,
- repo-wide blast radius,
- suggested tests,
- reviewer checklist,
- Orbit + LynkMesh context evidence.

## 2:20–2:40 — GitLab API dry-run

Run:

```bash
python -m app.main --mode gitlab_api --project-id demo/group --mr-iid 12 --dry-run
```

Show the generated GitLab MR notes endpoint.

## 2:40–3:00 — Close

Narration:

> Orbit Guardrail Agent is designed to make GitLab Duo workflows architecture-aware. Orbit provides GitLab-native context, and LynkMesh enriches the agent with graph-backed dependency and blast-radius evidence.

## Recording notes

- Use VS Code preview for Markdown so Unicode arrows and icons render correctly.
- Avoid showing tokens, private paths, browser cookies, or real customer data.
- Keep the final video under 3 minutes.
