param(
    [string]$OutDir = ".gitlab-demo-invoice-app"
)

$ErrorActionPreference = "Stop"

Write-Host "Preparing GitLab MR demo workspace at $OutDir"

if (Test-Path $OutDir) {
    Remove-Item -Recurse -Force $OutDir
}

New-Item -ItemType Directory -Force $OutDir | Out-Null
Copy-Item -Recurse -Force "demo/invoice_app_before/*" $OutDir

Push-Location $OutDir
try {
    git init
    git add .
    git commit -m "Initial clean invoice architecture"
    git checkout -b demo/controller-model-bypass
}
finally {
    Pop-Location
}

Copy-Item -Force \
    "demo/invoice_app_after_bad_mr/app/Http/Controllers/InvoiceController.php" \
    "$OutDir/app/Http/Controllers/InvoiceController.php"

Push-Location $OutDir
try {
    git add app/Http/Controllers/InvoiceController.php
    git commit -m "Bypass service layer in invoice controller"
    Write-Host ""
    Write-Host "Demo repo prepared. Next steps:"
    Write-Host "1. Add your GitLab remote."
    Write-Host "2. Push main and demo/controller-model-bypass branches."
    Write-Host "3. Open a Merge Request."
    Write-Host "4. Run Orbit Guardrail Agent in gitlab_api dry-run mode."
}
finally {
    Pop-Location
}
