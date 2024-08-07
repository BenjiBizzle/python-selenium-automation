# Created by B at 8/7/24
Feature: Tests for Help Page

  Scenario: user can select Help topic Technical support
    Given Open help page for Returns
    Then Verify Help Returns page opened
    When Select Help topic Technical Support
    Then Verify Technical Support page opened
