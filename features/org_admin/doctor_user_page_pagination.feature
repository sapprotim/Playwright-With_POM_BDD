Feature: Pagination Control

  Scenario: Fullerton Health Admin changes page size on doctor's user page and sees the table update accordingly
    Given the HPB Admin is logged in
    When the Admin selects the Doctor Admin role
    And the Admin selects a doctor user
    And the user selects different page sizes
    Then the table should reflect the selected page size