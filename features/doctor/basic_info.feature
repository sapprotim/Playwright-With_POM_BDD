Feature: Show user basic info

  Scenario: Doctor views a user's basic information from their profile
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the user checks the basic info
    Then the user age is shown