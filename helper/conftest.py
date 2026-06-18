import subprocess
import allure
import pytest


@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(request):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        driver = getattr(request.instance, "driver", None)
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


def pytest_sessionfinish(session, exitstatus):
    subprocess.run(
        ["allure", "generate", "allure-results", "-o", "allure-report", "--clean"],
        shell=True
    )
    subprocess.Popen(
        "start allure open allure-report",
        shell=True
    )