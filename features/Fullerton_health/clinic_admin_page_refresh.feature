Feature: refresh page

  Scenario: Fullerton Health Admin refreshes Clinic Admin page successfully
    Given the fullerton health admin is logged in
    When selects the Clinic Admin role
    And the user refreshes the page
    Then the page should be refreshed successfully









