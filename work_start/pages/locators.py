from selenium.webdriver.common.by import By


class MainPageLocators:
    VIEW_BASKET_FORM = (By.CSS_SELECTOR, "#default>header>div.page_inner>div>div.basket-mini.pull-right.hidden-xs"
                                         ">span>a")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDRESS_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form>button")

class ProductPageLocators:
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    NAME_OF_PRODUCT = (By.TAG_NAME, "h1")
    BASKET_VALUE = (By.CLASS_NAME, "alertinner>p>strong")
    PRODUCT_COST = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MESSAGE = [By.CSS_SELECTOR, "#messages>div:nth-child(1)"]


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_FORM = (By.CSS_SELECTOR, "#default>header>div.page_inner>div>div.basket-mini.pull-right.hidden-xs"
                                         ">span>a")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner>p')


class BasketPageLocators:
    BASKET_NOT_EMPTY = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_IS_NOT_EMPTY = (By.CSS_SELECTOR, '#content_inner>p')
