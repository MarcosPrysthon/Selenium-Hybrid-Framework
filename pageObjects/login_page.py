from selenium import webdriver

class LoginPage:
    textbox_username_id = 'Email'
    textbox_password_id = 'Password'
    button_login_xpath = '//button[text()="Log in"]'
    link_logout_xpath = '//*[@id="navbarText"]/ul/li[3]/a'

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element('id', self.textbox_username_id).clear()
        self.driver.find_element('id', self.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element('id', self.textbox_password_id).clear()
        self.driver.find_element('id', self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element('xpath', self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element('xpath', self.link_logout_xpath).click()