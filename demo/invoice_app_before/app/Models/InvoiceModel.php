<?php

namespace Demo\Models;

final class InvoiceModel
{
    public static function create(array $payload): array
    {
        return [
            'id' => $payload['id'] ?? 'demo-invoice-001',
            'customer_id' => $payload['customer_id'] ?? 'demo-customer-001',
            'amount' => $payload['amount'] ?? 100000,
            'period' => $payload['period'] ?? '2026-06',
            'status' => 'created',
        ];
    }
}
