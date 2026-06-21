Feature: Calendar function view

  Scenario: Doctor uses the calendar in the Patient Logs tab to select a date
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the navigates Trend to Patient Logs
    And the calendar filter should be visible
    Then the doctor should be able to select a date from the calendar