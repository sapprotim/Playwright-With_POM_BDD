Feature: Records page Navigation

  Scenario: Doctor navigates to the Records page to view user's record information
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the Doctor Admin navigates to Records page
    Then the Records page should be visible