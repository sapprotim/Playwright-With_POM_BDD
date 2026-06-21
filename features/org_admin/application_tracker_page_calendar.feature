Feature: Calendar Filter Functionality

  Scenario: Apply all calendar filter options and verify the filter is applied
    Given the HPB Admin is logged in
    When the user selects Application Tracker page
    And the user applies all calendar filter options
    Then the calendar filter should be applied