Feature: Organization View Tab Access

  Scenario: Clinic Admin accesses the Organization View tab for visibility
    Given the Clinic Admin is logged in
    When the Admin opens the Organization View tab
    Then the Organization View tab should be visible