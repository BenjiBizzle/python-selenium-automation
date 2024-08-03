from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "span.sc-58ad44c0-3.kwbrXj.h-margin-r-x3")
    SIGN_IN_SIDE_NAV_BTN = (By.XPATH, "//a[@data-test='accountNav-signIn']")

    def search_product(self, product):
        print('POM layer:', product)
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)

    def click_cart(self):
        self.wait_and_click(*self.CART_BTN)

    def click_sign_in(self):
        self.wait_and_click(*self.SIGN_IN_BTN)
        sleep(5)

    def click_sign_in_side_nav_button(self):
        self.wait_and_click(*self.SIGN_IN_SIDE_NAV_BTN)
        sleep(5)
