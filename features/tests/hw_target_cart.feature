# Created by B at 7/8/24.
Feature: Target Empty cart test


  Scenario:Verify cart is empty when clicking cart icon
    Given Open Target main page
    When Click on cart icon
    Then Verify Cart is Empty
