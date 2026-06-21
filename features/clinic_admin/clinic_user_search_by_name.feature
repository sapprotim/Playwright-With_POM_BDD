Feature: Search by Name functionality

  Scenario: Clinic Admin searches for a user by name
    Given the Clinic Admin is logged in
    When the user searches for a name
    Then the system should display the matching user
