Feature: refresh page

  Scenario: HPB Admin refreshes Clinic Admin page successfully
    Given the HPB Admin is logged in
    When the user selects Application Tracker page
    And the user refreshes the page
    Then the page should be refreshed successfully