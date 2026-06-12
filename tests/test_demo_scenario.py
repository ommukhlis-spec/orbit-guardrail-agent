from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def test_before_demo_uses_service_layer():
    controller = read("demo/invoice_app_before/app/Http/Controllers/InvoiceController.php")
    assert "$this->invoiceService->createInvoice($request)" in controller
    assert "InvoiceModel::create($request)" not in controller


def test_after_bad_mr_bypasses_service_layer():
    controller = read("demo/invoice_app_after_bad_mr/app/Http/Controllers/InvoiceController.php")
    assert "InvoiceModel::create($request)" in controller
    assert "Intentional bad MR for demo" in controller


def test_blast_radius_demo_files_exist():
    expected = [
        "demo/invoice_app_after_bad_mr/app/Services/InvoiceService.php",
        "demo/invoice_app_after_bad_mr/app/Services/BillingEngine.php",
        "demo/invoice_app_after_bad_mr/app/Services/ReportExportService.php",
    ]
    for rel in expected:
        assert (ROOT / rel).exists(), rel
