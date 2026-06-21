Feature: Search user profile by name

  Scenario: Doctor Admin searches and opens a user profile
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    Then the user profile should be opened