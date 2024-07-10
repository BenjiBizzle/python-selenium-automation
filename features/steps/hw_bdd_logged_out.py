from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# @given("Open Target main page")
# def target_page(context):
#     context.driver.get('https://www.target.com/')

@when("Click on Sign In")
def sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, ".sc-58ad44c0-3.kwbrXj.h-margin-r-x3").click()
    context.driver.find_element(By.CSS_SELECTOR, "#listaccountNav-signIn").click()
    sleep(5)

@then("Verify Sign In form opened")
def verify_sign_in(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, ".sc-fe064f5c-0.sc-315b8ab9-2.WObnm.gClYfs").text
    assert expected_text == actual_text
