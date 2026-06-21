Feature: search

  Scenario: Fullerton Health Admin searches for a user under 'All User' and views matching results
    Given the HPB Admin is logged in
    When the Admin opens the Users page
    And the user selects the All Users tab
    And the all user searches for a name
    Then the system should display the matching user