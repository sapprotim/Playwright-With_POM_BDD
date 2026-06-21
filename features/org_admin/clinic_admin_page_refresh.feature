Feature: refresh page

  Scenario: HPB Admin refreshes Clinic Admin page successfully
    Given the HPB Admin is logged in
    When selects the Clinic Admin role
    And the user refreshes the page
    Then the page should be refreshed successfully