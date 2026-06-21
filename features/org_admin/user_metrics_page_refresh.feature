Feature: refresh page

  Scenario: Fullerton Health Admin refreshes User Metrics page successfully
    Given the HPB Admin is logged in
    When the Admin opens the User Metrics page
    And the user refreshes the page
    Then the page should be refreshed successfully









