Feature: Pagination Control

  Scenario: Fullerton Health Admin selects Doctor, changes the page size and verifies table updates accordingly
    Given the HPB Admin is logged in
    When the Admin selects the Doctor Admin role
    And the user selects different page sizes
    Then the table should reflect the selected page size




