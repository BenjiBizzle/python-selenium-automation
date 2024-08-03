from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    CLICK_VIEW_CART_BTN = (By.CSS_SELECTOR, "[href='/cart']")
   #  CLICK_VIEW_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")

    def verify_cart_empty(self):
        self.wait_for_element_appear(*self.CART_EMPTY_MSG)
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def click_view_cart_btn(self):
        self.click(*self.CLICK_VIEW_CART_BTN)
