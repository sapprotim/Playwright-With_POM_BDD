Feature: Create Clinic

  Scenario: HPB Admin creates a new Clinic
    Given the HPB Admin is logged in
    When admin creates a Clinic
    Then the Clinic should be created successfully