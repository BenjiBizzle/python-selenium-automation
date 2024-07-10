from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# @given("Open Target main page")
# def target_page(context):
#     context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label*='car']").click()
    sleep(3)


@then('Verify Cart is Empty')
def verify_empty_cart(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, ".sc-fe064f5c-0.dtCtuk").text
    assert actual_text == expected_text
