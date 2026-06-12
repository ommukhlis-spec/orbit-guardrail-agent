<?php

namespace Demo\Services;

final class BillingEngine
{
    public function syncInvoice(array $invoice): void
    {
        // Downstream billing workflow expects invoices to be created through InvoiceService.
    }
}
