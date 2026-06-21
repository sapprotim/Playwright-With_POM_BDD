Feature: Pagination Control

  Scenario: Fullerton Health Admin selects Fullerton Health Admin page, changes the page size and verifies table updates accordingly
    Given the fullerton health admin is logged in
    When the Admin selects the Fullerton Health Admin role
    And the user selects different page sizes
    Then the table should reflect the selected page size




