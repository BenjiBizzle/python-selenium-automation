from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign In form opened')
def sign_into_text(context):
    context.app.sign_in_page.sign_into_text()
