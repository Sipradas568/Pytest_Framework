import pytest
from selenium import webdriver




@pytest.fixture()

def setup(request):
    
    driver = webdriver.Chrome()
    driver.get("https://translatelaw.gramener.com/login/?next=https%3A%2F%2Ftranslatelaw.gramener.com%2F") 
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()