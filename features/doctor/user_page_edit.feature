Feature: Doctor Edit User Functionality

  Scenario: Doctor edits a user profile and verifies the updated information
    Given the doctor Admin is logged in
    When the doctor selects and edits a user
    Then the user data should be updated and confirmed