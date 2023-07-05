from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    PATH = 'C:/Users/marcosvn/Documents/studies/ict/chromedriver.exe'

    if browser == 'chrome':
        driver = webdriver.Chrome(PATH)
    elif browser == 'firefox':
        driver = webdriver.Firefox(PATH)
    else:  # Default browser
        driver = webdriver.Chrome(PATH)
    return driver

def pytest_addoption(parser):    # This will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):            # This will return the browser to the setup method   
    return request.config.getoption('--browser')

# HTML Report
def pytest_configure(config):    # Hook for adding env info to HTML report
    config._metadata = {
        'Project name': 'nop Commerce',
        'Module name': 'Costumers',
        'Tester': 'Marcos'
    }