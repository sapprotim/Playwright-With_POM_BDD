
Feature: Access Public Board inside iframe

  Scenario: User fills passcode and accesses the public board
    Given the HPB Admin is logged in
    When the user selects Application Tracker page
    And the user clicks the Engagements
    And the user accesses the public board mobile
    Then the public board is visible