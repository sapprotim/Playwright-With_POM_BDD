Feature: refresh page

  Scenario: Fullerton Health Admin refreshes Doctor page successfully
    Given the fullerton health admin is logged in
    When the Admin selects the Doctor Admin role
    And the user refreshes the page
    Then the page should be refreshed successfully









