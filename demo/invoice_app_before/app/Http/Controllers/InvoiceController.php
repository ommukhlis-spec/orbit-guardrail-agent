<?php

namespace Demo\Http\Controllers;

use Demo\Services\InvoiceService;

final class InvoiceController
{
    public function __construct(
        private InvoiceService $invoiceService
    ) {}

    public function store(array $request): array
    {
        // Expected architecture: Controller -> Service -> Model.
        // The controller delegates business rules to InvoiceService.
        return $this->invoiceService->createInvoice($request);
    }
}
