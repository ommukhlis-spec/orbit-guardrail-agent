## 🛡️ Orbit Guardrail Briefing (powered by LynkMesh)

This MR changes 1 architecture-sensitive file(s):

- `app/Http/Controllers/InvoiceController.php`

### ⚠️ Architecture Guardrail Violation

**Rule:** `layering.controller_to_model_bypass`
**Violation:** Direct Model access detected from `InvoiceController::store` to `InvoiceModel::create`.

**Expected flow:** Controller → Service → Model
**Detected flow:** Controller → Model

Existing service candidate `InvoiceService` is bypassed by direct model access.

### 📊 Repo-Wide Blast Radius

LynkMesh context indicates this change may affect:

- `InvoiceService::createInvoice` — Existing service entrypoint bypassed
- `BillingEngine::syncInvoice` — Depends on normalized invoice creation flow
- `ReportExportService::monthlyInvoiceSummary` — Reads invoice state affected by creation flow

### 🧪 Suggested Test Coverage

- [ ] Invoice creation integration test
- [ ] Billing regression test
- [ ] Monthly invoice report export test

### ✅ Reviewer Checklist

- [ ] Confirm whether controller should delegate to `InvoiceService`
- [ ] Check that invoice creation still triggers billing sync
- [ ] Verify monthly report output after the change

**Context evidence:**

- Orbit source: MR changed files + code context
- LynkMesh context pack: `sha256:demo-context-pack`
