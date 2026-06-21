Feature: Lifestyle tab navigation

  Scenario: Doctor opens a user’s profile and navigates to the Lifestyle tab
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And navigates to the Lifestyle tab
    Then the Lifestyle tab should be opened