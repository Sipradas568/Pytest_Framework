import pytest
from selenium.webdriver.common.by import By
import time
from Config.config import BaseURL
from Pages.Login_page import LoginPage


class Testcase(BaseURL):


    def test_validLogin(self,setup):
        lp = LoginPage(setup)
        lp.ValidLogin("nidhi.chandra@gramener.com","0000")
        time.sleep(10)
        res = self.driver.fi
        print(res)
        Expected_Title = "TranslateLaw"
        assert res == Expected_Title
        assert True(res.__contains__("Project View"))