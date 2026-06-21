Feature: Pagination Control

  Scenario: Clinic Admin changes page size on the Doctor Admin page
    Given the Clinic Admin is logged in
    When the Admin selects the Doctor Admin role
    And the user selects different page sizes
    Then the table should reflect the selected page size




