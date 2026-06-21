Feature: Pagination Control

  Scenario: Fullerton Health Admin selects User Lists page, changes the page size and verifies table updates accordingly
    Given the HPB Admin is logged in
    When the Admin opens the Users page
    And the user selects the All Users tab
    And the user selects different page sizes
    Then the table should reflect the selected page size





