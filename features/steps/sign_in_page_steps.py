from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# @given('Open Target sign in page')
# def open_sign_in_page(context):
#     context.app.sign_in_page.open_sign_in_page()
#     sleep(4)


@then('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()


@then('Verify Sign In form opened')
def sign_into_text(context):
    context.app.sign_in_page.sign_into_text()


@then('Click on Target terms and conditions link')
def click_on_target_terms_and_conditions_link(context):
    context.app.sign_in_page.tc_link()
    sleep(4)


@then('Switch to the newly opened window')
def switch_window(context):
    context.app.terms_conditions_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.terms_conditions_page.verify_tc_url()


@then('User can close new window and switch back to original')
def close_and_switch_to_original(context):
    context.app.terms_conditions_page.close()
    context.app.terms_conditions_page.switch_to_window_by_id(context.original_window)
