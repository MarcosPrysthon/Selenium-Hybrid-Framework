from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class AddCostumer:
    sidebar_costumer_xpath = '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a'
    sidebar_costumer_option_xpath = '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a'
    button_add_new_xpath = '/html/body/div[3]/div[1]/form[1]/div/div/a'
    textbox_email_xpath = '//*[@id="Email"]'
    textbox_password_xpath = '//*[@id="Password"]'
    textbox_first_name_xpath = '//*[@id="FirstName"]'
    textbox_last_name_xpath = '//*[@id="LastName"]'
    radio_gender_male_xpath = '//*[@id="Gender_Male"]'
    radio_gente_female_xpath = '//*[@id="Gender_Female"]'
    textbox_date_birth_xpath = '//*[@id="DateOfBirth"]'
    textbox_company_name_xpath = '//*[@id="Company"]'
    radio_tax_xpath = '//*[@id="IsTaxExempt"]'
    textbox_newsletter_xpath = '//*[@id="customer-info"]/div[2]/div[9]/div[2]/div/div[1]/div/div'
    listitem_newsletter_1_xpath = '//*[@id="SelectedNewsletterSubscriptionStoreIds_listbox"]/li[1]'
    listitem_newsletter_2_xpath = '//*[@id="SelectedNewsletterSubscriptionStoreIds_listbox"]/li[2]'
    textbox_costumer_roles_xpath = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    listitem_cr_administrators_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[1]'
    listitem_cr_forum_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[2]'
    listitem_cr_guests_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[3]'
    listitem_cr_registered_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[4]'
    listitem_cr_vendors_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[5]'
    dropdown_vendor_xpath = '//*[@id="VendorId"]'
    textbox_admin_comment_xpath = '//*[@id="AdminComment"]'
    button_save_xpath = '/html/body/div[3]/div[1]/form/div[1]/div/button[1]'

    def __init__(self, driver):
        self.driver = driver

    def click_sidebar_costumers_menu(self):
        self.driver.find_element('xpath', self.sidebar_costumer_xpath).click()

    def click_sidebar_costumers_option(self):
        self.driver.find_element('xpath', self.sidebar_costumer_option_xpath).click()

    def click_add_new(self):
        self.driver.find_element('xpath', self.button_add_new_xpath).click()

    def set_email(self, email):
        self.driver.find_element('xpath', self.textbox_email_xpath).clear()
        self.driver.find_element('xpath', self.textbox_email_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element('xpath', self.textbox_password_xpath).clear()
        self.driver.find_element('xpath', self.textbox_password_xpath).send_keys(password)

    def set_costumer_roles(self, role):
        self.driver.find_element('xpath', self.textbox_costumer_roles_xpath).click()
        time.sleep(3)

        if role == 'Registered':
            self.list_item = self.driver.find_element('xpath', self.listitem_cr_registered_xpath)
        elif role == 'Administrators':
            self.list_item = self.driver.find_element('xpath', self.listitem_cr_administrators_xpath)
        elif role == 'Guest':
            # User cannot be Guest and Registered at the same time
            time.sleep(3)
            # Remove default value Registered
            self.driver.find_element('xpath', '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
            self.list_item = self.driver.find_element('xpath', self.listitem_cr_guests_xpath)
        elif role == 'Vendor':
            self.list_item = self.driver.find_element('xpath', self.listitem_cr_vendors_xpath)
        elif role == 'Forum':
            self.list_item = self.driver.find_element('xpath', self.listitem_cr_forum_xpath)

        time.sleep(3)
        self.driver.execute_script('arguments[0].click()', self.list_item)

    def set_newsletter(self, value):
        self.driver.find_element('xpath', self.textbox_newsletter_xpath).click()
        time.sleep(3)

        if value == 'Store 1':
            self.list_item = self.driver.find_element('xpath', self.listitem_newsletter_1_xpath)
        elif value == 'Store 2':
            self.list_item = self.driver.find_element('xpath', self.listitem_newsletter_2_xpath)

        time.sleep(3)
        self.driver.execute_script('arguments[0].click()', self.list_item)

    def set_manage_vendor(self, value):
        drop = Select(self.driver.find_element('xpath', self.dropdown_vendor_xpath))
        drop.select_by_visible_text(value)

    def set_gender(self, gender):
        if gender == 'Female':
            self.driver.find_element('xpath', self.radio_gente_female_xpath).click()
        else:
            self.driver.find_element('xpath', self.radio_gender_male_xpath).click()

    def set_first_name(self, fname):
        self.driver.find_element('xpath', self.textbox_first_name_xpath).clear()
        self.driver.find_element('xpath', self.textbox_first_name_xpath).send_keys(fname)

    def set_last_name(self, lname):
        self.driver.find_element('xpath', self.textbox_last_name_xpath).clear()
        self.driver.find_element('xpath', self.textbox_last_name_xpath).send_keys(lname)

    def set_date_birth(self, dob):
        self.driver.find_element('xpath', self.textbox_date_birth_xpath).clear()
        self.driver.find_element('xpath', self.textbox_date_birth_xpath).send_keys(dob)

    def set_tax_exempt(self, tax):
        checkbox = self.driver.find_element('xpath', self.radio_tax_xpath) 
        if tax and not checkbox.is_selected():
            checkbox.click()
        elif not tax and checkbox.is_selected():
            checkbox.click()

    def set_company_name(self, comname):
        self.driver.find_element('xpath', self.textbox_company_name_xpath).clear()
        self.driver.find_element('xpath', self.textbox_company_name_xpath).send_keys(comname)

    def set_admin_comment(self, comment):
        self.driver.find_element('xpath', self.textbox_admin_comment_xpath).clear()
        self.driver.find_element('xpath', self.textbox_admin_comment_xpath).send_keys(comment)

    def click_save(self):
        self.driver.find_element('xpath', self.button_save_xpath).click()