from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_PAGE_LINK = "https://selenium1py.pythonanywhere.com/accounts/login/"
