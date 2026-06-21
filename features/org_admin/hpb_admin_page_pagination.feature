Feature: Pagination Control

  Scenario: HPB Admin selects HPB admin, changes the page size and verifies table updates accordingly
    Given the HPB Admin is logged in
    When selects the HPB Admin role
    And the user selects different page sizes
    Then the table should reflect the selected page size




