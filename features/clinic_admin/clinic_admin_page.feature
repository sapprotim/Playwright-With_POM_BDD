Feature: Organization View Tab Access

  Scenario: Clinic Admin accesses the Organization View tab to view relevant info
    Given the Clinic Admin is logged in
    When selects the Clinic Admin role
    Then the Clinic Admin page is displayed