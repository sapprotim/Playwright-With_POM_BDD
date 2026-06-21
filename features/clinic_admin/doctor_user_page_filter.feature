Feature: Search by Name functionality

  Scenario: Clinic Admin filters doctor users by clinic
    Given the Clinic Admin is logged in
    When the Admin selects the Doctor Admin role
    And the Admin selects a doctor user
    And the admin filters users by clinic
    Then the filtered users should be displayed correctly
