from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_PAGE_URL = "https://selenium1py.pythonanywhere.com/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    NAME_OF_PRODUCT = (By.TAG_NAME, "h1")
    BASKET_VALUE = (By.CLASS_NAME, "alertinner>p>strong")
    PRODUCT_COST = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MESSAGE = [By.CSS_SELECTOR, "#messages>div:nth-child(1)"]


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")