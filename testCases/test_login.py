import pytest
from selenium import webdriver
from pageObjects.login_page import LoginPage

class Test_001_Login:
    base_URL = 'https://admin-demo.nopcommerce.com/'
    username = 'admin@yourstore.com'
    password = 'admin'

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        act_title = self.driver.title

        if act_title == 'Your store. Login':
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot('.\\screenshots\\'+'test_homePageTitle.png')
            self.driver.close()
            assert False

    def test_login(self, setup):
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
        else:
            self.driver.save_screenshot('.\\screenshots\\'+'test_login.png')
            self.driver.close()
            assert False

        self.driver.close()