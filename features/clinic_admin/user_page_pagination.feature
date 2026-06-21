Feature: Pagination Control

  Scenario: Clinic Admin access the Clinic Admin page size after login
    Given the Clinic Admin is logged in
    When the user selects different page sizes
    Then the table should reflect the selected page size




