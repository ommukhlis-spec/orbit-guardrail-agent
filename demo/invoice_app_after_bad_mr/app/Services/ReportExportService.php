<?php

namespace Demo\Services;

final class ReportExportService
{
    public function monthlyInvoiceSummary(string $period): array
    {
        // Report export depends on normalized invoice state produced by InvoiceService.
        return [
            'period' => $period,
            'status' => 'ready',
        ];
    }
}
