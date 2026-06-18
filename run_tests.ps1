# ============================
# Select Tests
# ============================

$runLogin      = $false
$runHome       = $false
$runProfile    = $true
$runInsurance  = $false
$runLogout     = $false

# Leave empty to run the entire InsuranceTest.py
$insuranceTest = "test_01_insurance_test"

# ============================
# Build Test List
# ============================

$testFiles = @()

if ($runLogin)      { $testFiles += "tests/LoginTest.py" }
if ($runHome)       { $testFiles += "tests/HomePageTest.py" }
if ($runProfile)    { $testFiles += "tests/ProfileSectionTest.py" }

if ($runInsurance) {
    if ([string]::IsNullOrWhiteSpace($insuranceTest)) {
        $testFiles += "tests/InsuranceTest.py"
    }
    else {
        $testFiles += "tests/InsuranceTest.py::InsuranceTest::$insuranceTest"
    }
}

if ($runLogout) { $testFiles += "tests/Logout.py" }

if ($testFiles.Count -eq 0) {
    Write-Host "❌ No tests selected."
    exit
}

# ============================
# Clean Previous Results
# ============================

if (Test-Path "allure-results") {
    Remove-Item "allure-results" -Recurse -Force
}

if (Test-Path "allure-report") {
    Remove-Item "allure-report" -Recurse -Force
}

# ============================
# Run Tests
# ============================

Write-Host ""
Write-Host "======================================="
Write-Host "Running Selected Test Cases..."
Write-Host "======================================="

$testFiles | ForEach-Object { Write-Host $_ }

pytest $testFiles -v -s --alluredir=allure-results

# ============================
# Generate Allure Report
# ============================

Write-Host ""
Write-Host "Generating Allure Report..."

allure generate allure-results --clean -o allure-report


# ============================
# Send Slack Notification
# ============================

Write-Host ""
Write-Host "Sending Slack Notification..."

.\.venv\Scripts\python.exe .\slack_notification.py

Write-Host "Slack notification completed."

# ============================
# Open Allure Report
# ============================

Write-Host ""
Write-Host "Opening Allure Report..."

allure serve allure-results

Write-Host ""
Write-Host "======================================="
Write-Host "Execution Completed Successfully"
Write-Host "======================================="