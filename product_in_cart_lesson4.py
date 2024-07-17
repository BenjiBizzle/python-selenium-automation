from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[id*='addToCartButtonOrTextId']")
ADD_TO_CART_BTN_2 = (By.XPATH, "//button[@data-test='orderPickupButton']")

@then("Add product into cart")
def add_product(context):
    # context.driver.find_element(By.XPATH, "//button[@id='addToCartButtonOrTextIdFor83374957']").click()
    # context.driver.find_element(By.XPATH, "//button[@data-test='orderPickupButton']").click()
    #sleep(7)
    context.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()
    context.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN_2)).click()


@then("Verify product has been added to cart")
def verify_product(context):
    expected_text = "Added to cart"
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Added to cart']").text
    assert actual_text == expected_text, f'Expected {expected_text}, got {actual_text}'
    sleep(4)
