Feature: Clinic User Edit

  Scenario: HPB Admin edits a user assigned to a clinic
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the clinic page
    And clicks Edit on a user and updates the user’s details
    Then the updated user information should appear in the user list