# ── Test Selection ────────────────────────────────────────────────────────────
$runLogin        = $false
$runHome         = $false
$runProfile      = $false
$runInsurance    = $false
$runCashDeposit  = $false
$runLogout       = $false
$runReferAndEarn = $false
$runAppSettings  = $true

# Specify a single test to run, or leave empty to run all tests in InsuranceTest.py
$insuranceTest  = "test_01_Insurance_Test"

# ── Build Test List ───────────────────────────────────────────────────────────
$testFiles = @()

if ($runLogin)         { $testFiles += "tests/LoginTest.py" }
if ($runHome)          { $testFiles += "tests/HomePageTest.py" }
if ($runProfile)       { $testFiles += "tests/ProfileSectionTest.py" }
if ($runInsurance)     { $testFiles += "tests/InsuranceTest.py" }
if ($runCashDeposit)   { $testFiles += "tests/CashDepositTest.py" }
if ($runLogout)        { $testFiles += "tests/Logout.py" }
if ($runReferAndEarn)  { $testFiles += "tests/ReferAndEarnTest.py" }
if ($runAppSettings)   { $testFiles += "tests/AppSettingsTest.py"}

if ($runInsurance) {
    if ([string]::IsNullOrWhiteSpace($InsuranceTest)) {
        $testFiles += "tests/InsuranceTest.py"
    } else {
        $testFiles += "tests/InsuranceTest.py::InsuranceTest::$InsuranceTest"
    }
}

if ($testFiles.Count -eq 0) {
    Write-Host "No tests selected. Set at least one `$run* flag to `$true." -ForegroundColor Red
    exit
}

# ── Clean Previous Results ────────────────────────────────────────────────────
@("allure-results", "allure-report") | ForEach-Object {
    if (Test-Path $_) { Remove-Item $_ -Recurse -Force }
}

# ── Run Tests ─────────────────────────────────────────────────────────────────
Write-Host "`n=======================================" -ForegroundColor Cyan
Write-Host " Running Selected Test Cases..."        -ForegroundColor Cyan
Write-Host "=======================================`n" -ForegroundColor Cyan

$testFiles | ForEach-Object { Write-Host "  $_" -ForegroundColor Yellow }

pytest $testFiles -v -s --alluredir=allure-results

# ── Generate Allure Report ────────────────────────────────────────────────────
Write-Host "`nGenerating Allure Report..." -ForegroundColor Cyan
allure generate allure-results --clean -o allure-report

# ── Send Slack Notification ───────────────────────────────────────────────────
Write-Host "`nSending Slack Notification..." -ForegroundColor Cyan
.\.venv\Scripts\python.exe .\slack_notification.py
Write-Host "Slack notification sent." -ForegroundColor Green

# ── Open Allure Report (opens the already-generated report, no re-generation) ─
Write-Host "`nOpening Allure Report..." -ForegroundColor Cyan
allure open allure-report

Write-Host "`n=======================================" -ForegroundColor Green
Write-Host " Execution Completed Successfully"       -ForegroundColor Green
Write-Host "=======================================`n" -ForegroundColor Green