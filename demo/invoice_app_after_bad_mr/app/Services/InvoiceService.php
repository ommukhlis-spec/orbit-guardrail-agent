<?php

namespace Demo\Services;

use Demo\Models\InvoiceModel;

final class InvoiceService
{
    public function __construct(
        private BillingEngine $billingEngine,
        private ReportExportService $reportExportService
    ) {}

    public function createInvoice(array $payload): array
    {
        $invoice = InvoiceModel::create($payload);

        $this->billingEngine->syncInvoice($invoice);
        $this->reportExportService->monthlyInvoiceSummary($invoice['period'] ?? 'unknown');

        return $invoice;
    }
}
