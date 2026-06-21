Feature: Calendar dropdown

  Scenario: Doctor Admin filters date by selecting a date range in calendar in the user profile
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And selects a start date and an end date
    Then the system should display data within the selected date range