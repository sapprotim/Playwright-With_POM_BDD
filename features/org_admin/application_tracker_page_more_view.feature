Feature: Application Tracker Log Actions

  Scenario: Open and close the first system log entry
    Given the HPB Admin is logged in
    When the user selects Application Tracker page
    And the user opens the first system log entry
    Then the user closes the system log popup