Feature: Calendar Functionality

  Scenario: Fullerton Health Admin navigates to "Prospects" page and selecting a date range and views the result
   Given the HPB Admin is logged in
   When selects the "Prospects" user
    And selects a start date and an end date
    Then the system should display data within the selected date range




