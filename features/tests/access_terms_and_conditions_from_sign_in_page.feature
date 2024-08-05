# Created by B at 8/4/24
Feature: Terms and conditions page

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target main page
    When Click on Sign In
    Then Click Sign In side nav button
    Then Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original