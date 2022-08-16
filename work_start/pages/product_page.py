from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_form = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_to_basket_form.click()

