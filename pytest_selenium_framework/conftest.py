from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from resources.framework.config import Config
from resources.pages.login import LoginPage
from resources.pages.base import BasePage
from resources.framework.utilities import TestData

g_driver = None
""" Setup : Initialize webdriver and visit the webpage
    Teardown : Close driver """
@pytest.fixture(autouse=True)
def suite_setup_and_teardown(request,browser):
    global g_driver
    if browser == "chrome" :
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    test_data_handle = TestData()
    base = BasePage(driver)
    request.cls.driver= driver
    g_driver = driver
    request.cls.test_data_handle= test_data_handle
    base.go_to(Config.URL)
    yield
    driver.quit()

""" Initialize login pages """
@pytest.fixture(autouse=True)
def test_setup_and_teardown(request):
    loginpage = LoginPage(request.cls.driver)
    request.cls.loginpage= loginpage

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session",autouse=True)
def browser(request):
    return request.config.getoption("--browser",default="chrome")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    global g_driver
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url(g_driver.current_url))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_name = Config.RESULTS_FOLDER + 'screenshot-%s.png' % now
            g_driver.save_screenshot(screenshot_name)
            if screenshot_name:
                html_append = '<div><img src="%s" alt="Error Screenshot" onclick="window.open(this.src)"></div>' % screenshot_name
            extra.append(pytest_html.extras.html(html_append))
        report.extra = extra