Feature: Create Clinic Admin User
  Scenario: Successfully create a new Clinic Admin
    Given the HPB Admin is logged in
    When selects the Clinic Admin role
    And Add a new Clinic Admin user
    And the user deletes a clinic Admin
    Then Clinic Admin successful deletion message should be shown