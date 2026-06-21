Feature: Validate Clinical and Lifestyle Wellness Scores

  Scenario: Doctor verifies Clinical and Lifestyle Wellness scores match expected calculations
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the Clinical and Lifestyle scores should be correctly displayed
    Then the Clinical and Lifestyle scores should be matched with the calculation
