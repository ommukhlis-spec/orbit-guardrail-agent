# Demo MR Diff — Service Layer Bypass

```diff
 use Demo\Services\InvoiceService;
+use Demo\Models\InvoiceModel;

 final class InvoiceController
 {
     public function store(array $request): array
     {
-        return $this->invoiceService->createInvoice($request);
+        return InvoiceModel::create($request);
     }
 }
```

This diff is intentionally small so the demo can show why local diff review is not enough. The guardrail agent adds repo-wide architecture context and blast-radius reasoning.
