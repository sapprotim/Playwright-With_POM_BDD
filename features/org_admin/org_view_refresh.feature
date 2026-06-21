Feature: Refresh page

  Scenario: HPB Admin refreshes the page
    Given the HPB Admin is logged in
    When the user refreshes the page
    Then the page should be refreshed successfully