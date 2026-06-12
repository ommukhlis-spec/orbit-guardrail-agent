# Demo Invoice App — After Bad MR

This folder represents an intentionally bad merge request used for the hackathon demo.

Detected flow:

```text
InvoiceController -> InvoiceModel
```

The controller bypasses `InvoiceService`, which means billing sync and report export side effects may be skipped or become inconsistent.
