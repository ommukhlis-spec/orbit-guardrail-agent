# Demo Merge Request Description

## Summary

This demo MR intentionally changes invoice creation in `InvoiceController.php`.

The bad change bypasses the existing service layer:

```text
Before: InvoiceController -> InvoiceService -> InvoiceModel
After:  InvoiceController -> InvoiceModel
```

## Why this matters

The local code diff may look small, but the architecture impact is larger:

- `InvoiceService::createInvoice` is bypassed.
- `BillingEngine::syncInvoice` may no longer run as expected.
- `ReportExportService::monthlyInvoiceSummary` may read inconsistent invoice state.

## Expected agent output

Orbit Guardrail Agent should produce a merge request briefing with:

- architecture guardrail violation,
- expected flow vs detected flow,
- repo-wide blast radius,
- suggested tests,
- reviewer checklist,
- Orbit + LynkMesh context evidence.
