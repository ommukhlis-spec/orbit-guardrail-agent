<?php

namespace Demo\Http\Controllers;

use Demo\Models\InvoiceModel;
use Demo\Services\InvoiceService;

final class InvoiceController
{
    public function __construct(
        private InvoiceService $invoiceService
    ) {}

    public function store(array $request): array
    {
        // Intentional bad MR for demo:
        // This bypasses InvoiceService and directly accesses the model.
        return InvoiceModel::create($request);
    }
}
