Feature: refresh page

  Scenario: Doctor refreshes the Records page successfully
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the Doctor Admin navigates to Records page
    And the user refreshes the page
    Then the page should be refreshed successfully







