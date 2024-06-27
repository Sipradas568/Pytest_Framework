import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from Config.config import BaseURL
from Pages.Login_page import LoginPage


class Testcase(BaseURL):


    def test_Valid_Login(self,setup):
        lp = LoginPage(setup)
        lp.Login("nidhi.chandra@gramener.com","0000")
        time.sleep(10)
        res = self.driver.find_element(By.CSS_SELECTOR,"ol[class = 'breadcrumb ml-2 bg-color-white fs-19 mb-0']")
        print(res.text)
        #Expected_Title = "TranslateLaw"
        #assert res == Expected_Title
        assert "Project View" in res.text