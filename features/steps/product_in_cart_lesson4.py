from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Add product into cart")
def add_product(context):
    context.driver.find_element(By.XPATH, "//button[@id='addToCartButtonOrTextIdFor83374957']").click()
    context.driver.find_element(By.XPATH, "//button[@data-test='orderPickupButton']").click()
    sleep(7)


@then("Verify product has been added to cart")
def verify_product(context):
    expected_text = "Added to cart"
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Added to cart']").text
    assert actual_text == expected_text, f'Expected {expected_text}, got {actual_text}'
    sleep(2)
