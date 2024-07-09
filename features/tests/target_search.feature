# Created by B at 7/2/24     This is  a Test Case
Feature: Target Main Page search tests

  Scenario: User can search for a product on Target
    Given Open Target main page
    When Search for product
    Then Verify search worked