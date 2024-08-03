from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SignInPage(Page):
    SIGN_INTO_TARGET_TXT = (By.CSS_SELECTOR, ".sc-fe064f5c-0.sc-315b8ab9-2.WObnm.gClYfs")

    def sign_into_txt(self):
        expected_text = 'Sign into your Target account'
        self.verify_text(expected_text, *self.SIGN_INTO_TARGET_TXT)
        sleep(5)
