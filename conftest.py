import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pytest_metadata.plugin import metadata_key


@pytest.fixture(scope="class")
def setupbrowser(request):
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    request.cls.driver = driver
    print("Launching  browser.........")
    yield
    print("closing  browser.........")
    driver.close()


"""

Below method is used to change title of automation report 

"""


def pytest_html_report_title(report):
    report.title = "Sandeep autotmation"


def pytest_configure(config):
    # config.stash[metadata_key]["TestEnvironment"] = "Production"
    from pytest_metadata.plugin import metadata_key
    @pytest.hookimpl(tryfirst=True)
    def pytest_sessionfinish(session, exitstatus):
        session.config.stash[metadata_key]["foo"] = "bar"


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
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

