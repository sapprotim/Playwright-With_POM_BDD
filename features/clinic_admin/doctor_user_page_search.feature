Feature: Search by Name functionality

  Scenario: Clinic Admin searches for a user by name on the doctor user page
    Given the Clinic Admin is logged in
    When the Admin selects the Doctor Admin role
    And the Admin selects a doctor user
    And the user searches for a name
    Then the system should display the matching user
