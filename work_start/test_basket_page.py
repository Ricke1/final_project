from .pages.basket_page import BasketPage
import pytest

def test_basket_is_empty(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
    page = BasketPage(browser, link)
    page.open()
    page.basket_is_empty()


@pytest.mark.xfail(strict=True)
def test_basket_is_not_empty(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
    page = BasketPage(browser, link)
    page.open()
    page.basket_is_not_empty()
