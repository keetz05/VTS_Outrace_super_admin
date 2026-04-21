from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def setup(browser):

    if browser == "chrome":
        options = Options()
        options.binary_location = "/usr/bin/chromium-browser"   # ✅ CORRECT PATH

        service = Service("/usr/bin/chromedriver")   # ✅ after install
        driver = webdriver.Chrome(service=service, options=options)

        print("Launching Chrome browser")

    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launching Edge browser")

    else:
        raise Exception("Browser not supported")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# ------ pytest html report ----------

def pytest_configure(config):
    if hasattr(config, "_metadata"):
        config._metadata['Project Name'] = 'Orange HRM'
        config._metadata['Module Name'] = 'Login Page'
        config._metadata['Tester Name'] = 'Keerthana'


def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)