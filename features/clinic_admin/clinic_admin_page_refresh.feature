Feature: refresh page

  Scenario: Clinic Admin refreshes the page successfully
    Given the Clinic Admin is logged in
    When selects the Clinic Admin role
    And the user refreshes the page
    Then the page should be refreshed successfully







