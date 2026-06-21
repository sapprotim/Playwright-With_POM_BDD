Feature: refresh page

  Scenario: Clinic Admin refreshes the Organization View tab successfully
    Given the Clinic Admin is logged in
    When the Admin opens the Organization View tab
    And the user refreshes the page
    Then the page should be refreshed successfully







