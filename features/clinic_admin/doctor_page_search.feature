Feature: Search by Name functionality

  Scenario: Clinic Admin searches for a user by name on the Doctor Admin page
    Given the Clinic Admin is logged in
    When the Admin selects the Doctor Admin role
    And the doctor searches for a name
    Then the system should display the matching user
