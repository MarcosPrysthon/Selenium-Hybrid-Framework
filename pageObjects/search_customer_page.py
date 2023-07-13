from selenium import webdriver
import time

class SearchCustomer:
    textbox_email_id = 'SearchEmail'
    textbox_first_name_id = 'SearchFirstName'
    textbox_last_name_id = 'SearchLastName'
    button_search_id = 'search-customers'
    table_search_results_xpath = '//*[@id="customers-grid"]'
    # tbody_table_body_xpath = '//*[@id="customers-grid"]/tbody'
    table_rows_xpath = '//*[@id="customers-grid"]/tbody/tr'
    table_columns_xpath = '//*[@id="customers-grid"]/tbody/tr/td'

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element('id', self.textbox_email_id).clear()
        self.driver.find_element('id', self.textbox_email_id).send_keys(email)

    def set_first_name(self, fname):
        self.driver.find_element('id', self.textbox_first_name_id).clear()
        self.driver.find_element('id', self.set_first_name).send_keys(fname)

    def set_last_name(self, lname):
        self.driver.find_element('id', self.set_last_name).clear()
        self.driver.find_element('id', self.set_last_name).send_keys(lname)

    def click_search(self):
        self.driver.find_element('id', self.button_search_id).click()

    def get_n_rows(self):
        return len(self.driver.find_elements('xpath', self.table_rows_xpath))

    def get_n_columns(self):
        return len(self.driver.find_elements('xpath', self.table_columns_xpath))

    def search_customer_email(self, exp_email):
        found = False

        for r in range(1, self.get_n_rows + 1):
            email_xpath = '//*[@id="customers-grid"]/tbody/tr[{id}]/td[2]'.format(id = r)
            table = self.driver.find_element('xpath', self.table_search_results_xpath)
            act_email = table.find_element('xpath', email_xpath).text
            if act_email == exp_email:
                found = True
                break
        
        return found

    def search_customer_name(self, exp_name):
        found = False

        for r in range(1, self.get_n_rows + 1):
            name_xpath = '//*[@id="customers-grid"]/tbody/tr[{id}]/td[3]'.format(id = r)
            table = self.driver.find_element('xpath', self.table_search_results_xpath)
            act_name = table.find_element('xpath', name_xpath).text
            if act_email == exp_name:
                found = True
                break
        
        return found