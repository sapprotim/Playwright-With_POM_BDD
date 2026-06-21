Feature: refresh page

  Scenario: HPB Admin refreshes Clinic User page successfully
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the clinic page
    And the user refreshes the page
    Then the page should be refreshed successfully