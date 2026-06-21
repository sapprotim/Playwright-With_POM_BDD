Feature: Wellness plan navigation

  Scenario: Doctor navigates to the Wellness plan page to view user's Wellness plan information
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the Doctor Admin navigates to the WP page
    Then the WP page should be visible