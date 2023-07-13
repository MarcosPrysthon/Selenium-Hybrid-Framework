import pytest
from selenium import webdriver
from pageObjects.login_page import LoginPage
from pageObjects.add_costumer_page import AddCustomer
from utilities.read_propeerties import ReadConfig
from utilities.custom_logger import LogGen
from utilities.email_generator import random_generator

class Test_003_AddCostumer:
    base_URL = ReadConfig.get_application_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.log_gen()

    def test_add_costumer(self, setup):
        self.logger.info('************** Test_003_AddCostumer **************')
        self.driver = setup
        self.driver.get(self.base_URL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.add_cust = AddCustomer(self.driver)

        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info('************** Login Succesful **************')

        self.logger.info('************** Starting Add Customer Test **************')

        self.add_cust.click_sidebar_costumers_menu()
        self.add_cust.click_sidebar_costumers_option()
        self.add_cust.click_add_new()

        self.logger.info('************** Providing Customer Info **************')

        self.email = random_generator() + '@gmail.com'
        self.add_cust.set_email(self.email)
        self.add_cust.set_password('gatomia123')
        self.add_cust.set_first_name('Marcos')
        self.add_cust.set_last_name('Prysthon')
        self.add_cust.set_gender('Male')
        self.add_cust.set_date_birth('1/06/1999')
        self.add_cust.set_company_name('NescoLTDA')
        self.add_cust.set_tax_exempt(True)
        self.add_cust.set_newsletter('Store 1')
        self.add_cust.set_costumer_roles('Guest')
        self.add_cust.set_manage_vendor('Vendor 1')
        self.add_cust.set_admin_comment('This is for testing....')
        self.add_cust.click_save()

        self.logger.info('************** Saving Customer Info **************')
        self.logger.info('************** Add Customer Validation Started **************')

        self.msg = self.driver.find_element('tag name', 'body').text

        if 'customer has been added successfully' in self.msg:
            assert True
            self.logger.info('************** Add Customer Test Passed **************')
        else:
            self.driver.save_screenshot('.\\screenshots\\' + 'test_add_customer_scr.png')
            self.logger.info('************** Add Customer Test Failed **************')
            assert False

        self.driver.close()
        self.logger.info('************** Ending Test_003_AddCostumer Test **************')