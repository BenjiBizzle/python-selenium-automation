from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("target circle page")
def circle_page(context):
    context.driver.get("https://www.target.com/circle")
    sleep(5)


@when("Locate the 10 benefit cells")
def benefit_cells(context):
    context.driver.find_elements(By.CSS_SELECTOR, ".sc-fb3945a7-5")


@then("Verify there is {number} benefit cells on the page")
def verify_benefit_cells(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, ".sc-fb3945a7-5")
    assert len(links) == number, f'Expected {number} benefit cells, got {len(links)}'
