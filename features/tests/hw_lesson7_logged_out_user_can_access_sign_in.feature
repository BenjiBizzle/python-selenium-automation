# Created by B at 8/1/24
Feature: Target logged out user can navigate to Sign In


  Scenario: Verify that a logged out user can navigate to Sign In
    Given Open target main page
    When Click on Sign In
    Then Click Sign In side nav button
    Then Verify Sign In form opened 