Feature: Doctor Account Creation

  Scenario: Successfully create a new Doctor account
    Given the HPB Admin is logged in
    When the Admin selects the Doctor Admin role
    And create a new Doctor
    Then the Doctor should be created successfully