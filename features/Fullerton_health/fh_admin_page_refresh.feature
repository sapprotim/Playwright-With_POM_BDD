Feature: refresh page

  Scenario: Fullerton Health Admin refreshes Fullerton Health Admin page successfully
    Given the fullerton health admin is logged in
    When the Admin selects the Fullerton Health Admin role
    And the user refreshes the page
    Then the page should be refreshed successfully









