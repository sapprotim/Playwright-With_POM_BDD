Feature: User Lists Page Access

  Scenario: Fullerton Health Admin opens Users page
    Given the HPB Admin is logged in
    When the Admin opens the Users page
    Then the Users page should be displayed