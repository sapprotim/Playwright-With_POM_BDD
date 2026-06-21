Feature: Application Tracker Engagements Access

  Scenario: User clicks Engagements tab from Application Tracker
    Given the HPB Admin is logged in
    When the user selects Application Tracker page
    And the user clicks the Engagements
    Then the Engagements section is displayed