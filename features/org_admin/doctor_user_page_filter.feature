Feature: Filter functionality

  Scenario: Fullerton Health Admin searches users by clinic after selecting Doctor role and sees correct filtered results
    Given the HPB Admin is logged in
    When the Admin selects the Doctor Admin role
    And the Admin selects a doctor user
    When the admin filters users by clinic
    Then the filtered users should be displayed correctly
