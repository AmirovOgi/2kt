import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    current_url = "https://demo-opencart.ru/"

    if browser_name == "chrome":
        driver = webdriver.Chrome(options=Options())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(options=FirefoxOptions())
    else:
        raise Exception("Driver not supported")

    driver.maximize_window()
    driver.get(current_url)
    driver.test_name = request.node.name

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
