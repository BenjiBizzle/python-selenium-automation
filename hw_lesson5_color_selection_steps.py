from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, ".sc-a26a6bf9-3.kobkMm")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent']")


@given('Open target product {product_id} page')
def open_target_product(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(5)


@then('Verify user can click through colors')
def search_through_colors(context):
    expected_colors = ['Cosmic Red', 'Midnight Black', 'White/Black', 'Starlight Blue', 'Galactic Purple', 'Gray',
                       'Cobalt Blue', 'Volcanic Red', 'Sterling Silver', 'Nova Pink - Out of Stock', 'Black | Red - Sold out']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
