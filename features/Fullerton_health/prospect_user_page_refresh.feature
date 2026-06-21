Feature: refresh page

  Scenario: Fullerton Health Admin refreshes Prospects page successfully
    Given the fullerton health admin is logged in
    When selects the "Prospects" user
    And the user refreshes the page
    Then the page should be refreshed successfully