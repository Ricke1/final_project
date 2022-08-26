from .base_page import BasePage
from .locators import BasketPageLocators
import pytest


class BasketPage(BasePage):

    def basket_is_not_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), "basket is empty, that's a negative test"

    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_NOT_EMPTY), "basket isn't empty"
