from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for product')
def search_product(context):
    #find search field and enter text
    context.driver.find_element(By.ID, "search").send_keys('tea')
    #click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    #wait for the page with search results to load
    sleep(6)

@then('Verify search worked')
def verify_search_worked(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//span[@class='h-text-bs h-display-flex h-flex-align-center h-text-grayDark h-margin-l-x2']").text
    assert expected_text in actual_text, f'Expected {expected_text}, got {actual_text}'