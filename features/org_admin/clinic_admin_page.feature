Feature: Clinic Admin Access

  Scenario: HPB Admin selects Clinic Admin role and views the Clinic Admin page
    Given the HPB Admin is logged in
    When selects the Clinic Admin role
    Then the Clinic Admin page is displayed