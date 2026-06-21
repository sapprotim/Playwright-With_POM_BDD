Feature: Pagination Control

  Scenario: Clinic Admin changes the page size to control number of records displayed
    Given the Clinic Admin is logged in
    When selects the Clinic Admin role
    And the user selects different page sizes
    Then the table should reflect the selected page size




