from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
import selenium


class ProductPage(BasePage):

    def add_to_basket(self):
        name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        add_to_basket_form = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_to_basket_form.click()
        print(f"Товар {name_of_product} добавлен в корзину")

    def check_basket_price(self):
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        print(f"Сумма в корзине: {basket_value}. Цена товара: {product_cost}")
        assert basket_value == product_cost, "Цена корзины не равна цене товара"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message isn't presented, that's a negative test"
