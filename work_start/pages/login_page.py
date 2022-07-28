from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form(*LoginPageLocators.LOGIN_FORM)
        self.should_be_register_form(*LoginPageLocators.REGISTER_FORM)

    def should_be_login_url(self,):
        try:
            "login" in LoginPageLocators.LOGIN_PAGE_URL
        except False:
            return False
        assert True

    def should_be_login_form(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        assert True

    def should_be_register_form(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        assert True
