import os

import pytest
import pytest_html

from appium.webdriver import Remote

driver = None


@pytest.fixture(scope="session", autouse=True)
def setup():
    global driver
    capabilities = {
        'platformName': 'Android',
        'platformVersion': '12',
        'deviceName': 'Samsung Galaxy M31',
        'appPackage': 'com.bolt.deliveryclient',
        'appActivity': 'com.boltdeliveryclientapp.MainActivity',
        'noReset': 'true',
        'newCommandTimeout': 240,
        'automationName': 'uiautomator2'
    }
    if driver is None:
        driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
        driver.update_settings({"waitForIdleTimeout": 240})
        yield driver
        driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


def pytest_html_report_title(report):
    report.title = "Automation_test_report"
