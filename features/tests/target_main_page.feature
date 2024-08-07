Feature: Target main page search tests

  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search results shown for coffee
    Then Verify correct search results URL opens for coffee


  Scenario: User can search for a mug
    Given Open target main page
    When Search for mug
    Then Verify search results shown for mug
    Then Verify correct search results URL opens for mug


  Scenario: User can search for an iphone
    Given Open target main page
    When Search for iphone
    Then Verify search results shown for iphone
    And Verify correct search results URL opens for iphone


  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search results shown for <expected_result>
    And Verify correct search results URL opens for <expected_result>
    Examples:
    |product  |expected_result    |
    |coffee   |coffee             |
    |tea      |tea                |
    |iphone   |iphone             |


  Scenario: User can add a product to cart
    Given Open target main page
    When Search for mug
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    When Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image

  Scenario: