
from Config.config import BaseURL
from Pages.Login_Locators import LoginLocators

from selenium.webdriver.common.by import By


class LoginPage(BaseURL):
    def __init__(self,driver):
        self.driver = driver
        self.loc = LoginLocators()

    def Login(self,un,pwd):
        self.un=un
        self.pwd=pwd
    
        self.driver.find_element(By.ID,self.loc.user_name).send_keys(self.un)
        self.driver.find_element(By.ID,self.loc.password).send_keys(self.pwd)
        self.driver.find_element(By.XPATH,self.loc.Submit).click()
        
