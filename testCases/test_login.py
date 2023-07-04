import pytest
from selenium import webdriver
from pageObjects.login_page import LoginPage
from utilities.read_propeerties import ReadConfig
from utilities.custom_logger import LogGen

class Test_001_Login:
    base_URL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    
    logger = LogGen.log_gen()

    def test_homePageTitle(self, setup):
        self.logger.info('************** Test_001_Login **************')
        self.logger.info('************** Verifying Home Page Title **************')

        self.driver = setup
        self.driver.get(self.base_URL)
        act_title = self.driver.title

        if act_title == 'Your store. Login':
            self.driver.close()
            assert True
            self.logger.info('************** Home Page Title Test Passed **************')
        else:
            self.driver.save_screenshot('.\\screenshots\\'+'test_homePageTitle.png')
            self.driver.close()
            assert False
            self.logger.error('************** Home Page Title Test Failed **************')

    def test_login(self, setup):
        self.logger.info('************** Verifying Login Test **************')
        self.driver = setup
        self.driver.get(self.base_URL)

        self.lp = LoginPage(self.driver)

        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        act_title = self.driver.title

        if act_title == 'Dashboard / nopCommerce administration':
            self.driver.close()
            assert True
            self.logger.info('************** Login Test Passed **************')
        else:
            self.driver.save_screenshot('.\\screenshots\\'+'test_login.png')
            self.driver.close()
            assert False
            self.logger.error('************** Login Test Failed **************')