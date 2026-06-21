Feature: Pagination Control

  Scenario: Fullerton Health Admin selects Prospects page, changes the page size and verifies table updates accordingly
    Given the fullerton health admin is logged in
    When selects the "Prospects" user
    And the user selects different page sizes
    Then the table should reflect the selected page size




