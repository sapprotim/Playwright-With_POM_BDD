Feature: Pagination Control

  Scenario: Fullerton Health Admin selects Zendesk user Page, changes the page size and verifies table updates accordingly
    Given the fullerton health admin is logged in
    When the Admin opens the Zendesk Users page
    And the user selects different page sizes
    Then the table should reflect the selected page size




