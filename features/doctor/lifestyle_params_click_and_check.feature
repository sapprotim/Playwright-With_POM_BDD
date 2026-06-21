Feature: View and check lifestyle parameters

  Scenario: Doctor opens a user’s profile to review lifestyle parameters
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And navigates to the Lifestyle tab
    And checks the lifestyle parameters
    Then the lifestyle parameters are shown

