Feature: Calendar Functionality

  Scenario: Fullerton Health Admin selects User Metrics page and selecting a date range and views the result
    Given the HPB Admin is logged in
    When the Admin opens the User Metrics page
    And selects a start date and an end date
    Then the system should display data within the selected date range