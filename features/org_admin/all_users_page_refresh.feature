Feature: refresh page

  Scenario: Fullerton Health Admin refreshes User Lists page successfully
    Given the HPB Admin is logged in
    When the Admin opens the Users page
    And the user selects the All Users tab
    And the user refreshes the page
    Then the page should be refreshed successfully









