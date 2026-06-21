Feature: View and check clinical parameters

  Scenario: Doctor opens a user’s profile to review clinical parameters
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And checks the clinical parameters
    Then the clinical parameters are shown

