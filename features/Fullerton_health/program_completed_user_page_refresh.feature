Feature: refresh page

  Scenario: Fullerton Health Admin refreshes Programme Completed User Lists page successfully
    Given the fullerton health admin is logged in
    When the Admin opens the Users page
    And the user selects the Programme Completed Users tab
    And the user refreshes the page
    Then the page should be refreshed successfully









