from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        assert self.should_be_login_url(), "Wrong login url"
        assert self.should_be_login_form(*LoginPageLocators.LOGIN_FORM), "No login form at the login page"
        assert self.should_be_register_form(*LoginPageLocators.REGISTER_FORM), "No register form at the login page"

    def should_be_login_url(self):
        A = self.browser.current_url
        if 'login' in A.split("/"):
            print(A.split("/"))
            return True
        else:
            return False

    def should_be_login_form(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_register_form(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD1_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        time.sleep(5)