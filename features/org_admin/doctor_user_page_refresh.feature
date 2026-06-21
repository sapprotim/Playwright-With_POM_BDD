Feature: refresh page

  Scenario: Fullerton Health Admin refreshes doctor's user page successfully
    Given the HPB Admin is logged in
    When the Admin selects the Doctor Admin role
    And the Admin selects a doctor user
    And the user refreshes the page
    Then the page should be refreshed successfully