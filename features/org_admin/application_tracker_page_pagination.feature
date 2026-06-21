Feature: Pagination Control

  Scenario: HPB Admin selects Clinic Admin, changes the page size and verifies table updates accordingly
    Given the HPB Admin is logged in
    When the user selects Application Tracker page
    And the user selects different page sizes
    Then the table should reflect the selected page size