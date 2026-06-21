Feature: Patient Logs tab view

  Scenario: Doctor opens a user’s profile navigates to and views the Patient Logs tab
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the navigates Trend to Patient Logs
    Then the Patient Logs page should be visible