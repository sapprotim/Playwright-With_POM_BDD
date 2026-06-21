Feature: Show user body info

  Scenario: Doctor views a user's body information from profile
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the user checks the body info
    Then the user body info is shown
