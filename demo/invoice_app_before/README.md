# Demo Invoice App — Before

This folder represents the expected architecture before the bad merge request.

Expected flow:

```text
InvoiceController -> InvoiceService -> InvoiceModel
```

The controller delegates invoice creation to `InvoiceService`, which centralizes billing sync and report export side effects.
