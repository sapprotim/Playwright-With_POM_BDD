Feature: View and check Generate Wellness Plan button in Trends

  Scenario: Doctor clicks the Generate Wellness Plan button in Trends and verifies it functions properly
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the admin clicks the Generate Wellness Plan button
    Then Button should work properly