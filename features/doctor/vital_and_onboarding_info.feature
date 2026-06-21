Feature: Show vital and onboarding info

  Scenario: Doctor views a user's user's vital and onboarding information
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the user checks the vital signs, last updated and onboarding info
    Then the vital signs, last updated and onboarding info is shown
