Feature: search

  Scenario: Fullerton Health Admin searches for a user under "User" and views matching results
    Given the fullerton health admin is logged in
    When the Admin opens the Users page
    And the user searches for a name
    Then the system should display the matching user