Feature: refresh page

  Scenario: Clinic Admin refreshes the Doctor Admin page successfully
    Given the Clinic Admin is logged in
    When the Admin selects the Doctor Admin role
    And the user refreshes the page
    Then the page should be refreshed successfully



