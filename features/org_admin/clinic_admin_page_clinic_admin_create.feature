Feature: Create Clinic Admin User
  Scenario: Successfully create a new Clinic Admin
    Given the HPB Admin is logged in
    When selects the Clinic Admin role
    And Add a new Clinic Admin user
    Then the Clinic Admin should be created successfully