from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SignInPage(Page):
    SIGN_INTO_TARGET_TXT = (By.CSS_SELECTOR, ".sc-fe064f5c-0.sc-315b8ab9-2.WObnm.gClYfs")
    TERMS_CONDITIONS_LINK = (By.CSS_SELECTOR, "[aria-label='terms & conditions - opens in a new window']")

    def store_original_window(self):
        self.open_url('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default'
                      '&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions'
                      '=create_session_signin')

    def sign_into_txt(self):
        expected_text = 'Sign into your Target account'
        self.verify_text(expected_text, *self.SIGN_INTO_TARGET_TXT)
        sleep(5)

    def tc_link(self):
        self.driver.find_element(*self.TERMS_CONDITIONS_LINK).click()
