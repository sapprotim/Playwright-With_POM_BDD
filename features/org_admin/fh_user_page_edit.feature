Feature: Fullerton Health User Edit

  Scenario: HPB Admin edits a user assigned to a Fullerton Health
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the Fullerton Health page
    And clicks Edit on a user and updates the user’s details
    Then the updated user information should appear in the user list