import pytest
from selenium import webdriver



@pytest.fixture()

def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "FF":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        driver = webdriver.Ie()
    
    driver.get("https://translatelaw.gramener.com/login/?next=https%3A%2F%2Ftranslatelaw.gramener.com%2F") 
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")