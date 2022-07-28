from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePage):
    def should_be_login_page(self):
        assert self.should_be_login_url(), "Wrong login url"
        assert self.should_be_login_form(*LoginPageLocators.LOGIN_FORM), "No login form at the login page"
        assert self.should_be_register_form(*LoginPageLocators.REGISTER_FORM), "No register form at the login page"

    def should_be_login_url(self,):
        try:
            assert "login" in LoginPageLocators.LOGIN_PAGE_URL
        except False:
            return False
        return True

    def should_be_login_form(self, how, what):
        try:
            Login_form = self.browser.find_element(how, what)
            print(Login_form)
        except NoSuchElementException:
            return False
        return True

    def should_be_register_form(self, how, what):
        try:
            Register_form = self.browser.find_element(how, what)
            print(Register_form)
        except NoSuchElementException:
            return False
        return True
