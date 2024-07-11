# Created by B at 7/10/24
Feature: Target circle page

  Scenario: User will be able to identify 10 benefit cells
    Given target circle page
    When Locate the 10 benefit cells
    Then Verify there is 10 benefit cells on the page