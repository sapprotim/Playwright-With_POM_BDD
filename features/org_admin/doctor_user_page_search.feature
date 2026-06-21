Feature: Search by Name functionality

  Scenario: Fullerton Health Admin searches for a user by name in Doctor user's page and views matching results
    Given the HPB Admin is logged in
    When the Admin selects the Doctor Admin role
    And the Admin selects a doctor user
    And the user searches for a name
    Then the system should display the matching user
