

Feature: Doctor User Selection

  Scenario: Clinic Admin selects a doctor user and views the doctor user page
    Given the Clinic Admin is logged in
    When the Admin selects the Doctor Admin role
    And the Admin selects a doctor user
    Then the doctor user page is displayed