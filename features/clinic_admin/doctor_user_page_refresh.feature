Feature: refresh page

  Scenario: Clinic Admin refreshes the doctor user page successfully
    Given the Clinic Admin is logged in
    When the Admin selects the Doctor Admin role
    And the Admin selects a doctor user
    And the user refreshes the page
    Then the page should be refreshed successfully



