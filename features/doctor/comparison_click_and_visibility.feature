Feature: Comparison section visibility

  Scenario: Doctor opens a user’s profile to review comparison section
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And clicks on the comparison section
    Then the comparison section becomes visible