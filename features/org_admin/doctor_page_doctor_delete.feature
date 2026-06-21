Feature: Doctor Account Creation

  Scenario: Successfully create a new Doctor account
    Given the HPB Admin is logged in
    When the Admin selects the Doctor Admin role
    And create a new Doctor
    And the user deletes a Doctor Admin
    Then Doctor Admin successful deletion message should be shown


