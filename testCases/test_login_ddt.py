import pytest
import time
from selenium import webdriver
from pageObjects.login_page import LoginPage
from utilities.read_propeerties import ReadConfig
from utilities.custom_logger import LogGen
from utilities import xl_utils

class Test_002_DDT_Login:
    base_URL = ReadConfig.get_application_url()
    data_file_path = '.\\testData\\LoginData.xlsx' 
    
    logger = LogGen.log_gen()

    def test_login_DDT(self, setup):
        self.logger.info('************** Test_002_DDT_Login **************')
        self.logger.info('************** Verifying Login DDT Test **************')
        self.driver = setup
        self.driver.get(self.base_URL)

        self.lp = LoginPage(self.driver)

        self.rows = xl_utils.getRowCount(self.data_file_path, 'Sheet1')

        list_status = []
        for i in range(2, self.rows+1):
            self.username = xl_utils.readData(self.data_file_path, 'Sheet1', i, 1)
            self.password = xl_utils.readData(self.data_file_path, 'Sheet1', i, 2)
            self.expect = xl_utils.readData(self.data_file_path, 'Sheet1', i, 3)

            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if act_title == exp_title:
                if self.expect == 'Pass':
                    self.logger.info('************** Login Passed **************') 
                    self.lp.click_logout()
                    list_status.append('Pass')
                elif self.expect == 'Fail':
                    self.logger.info('************** Login Failed **************')
                    self.lp.click_logout()
                    list_status.append('Fail')
            else:
                if self.expect == 'Pass':
                    self.logger.info('************** Login Failed **************') 
                    list_status.append('Fail')
                elif self.expect == 'Fail':
                    self.logger.info('************** Login Passed **************')
                    list_status.append('Pass')

        if 'Fail' not in list_status:
            self.logger.info('************** Login DDT test Passed **************')
            self.driver.close()
            assert True
        else:
            self.logger.info('************** Login DDT test Failed **************')
            self.driver.close()
            assert False
        
        self.logger.info('************** End of Test_002_DDT_Login **************')