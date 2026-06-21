Feature: search

  Scenario: HPB Admin searches for a user by name in Fullerton Health Doctor page and views matching results
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the Fullerton Health page
    And selects doctor to view its doctors
    And the FH doctor searches for a name
    Then the system should display the matching user