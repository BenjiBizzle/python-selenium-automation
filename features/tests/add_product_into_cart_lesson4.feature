# Created by B at 7/10/24
Feature:  Target product in cart

  Scenario:  Add any Target’s product into the cart, and make sure it’s there
    Given Open target main page
    When Search for product
    Then Add product into cart
    Then Verify product has been added to cart