Feature: Edit Fullerton Health Admin user

  Scenario: Edit an existing Fullerton Health Admin user's details
    Given the HPB Admin is logged in
    When the Admin selects the Fullerton Health Admin role
    And Add a new Fullerton Health Admin user
    And the user edits a Fullerton Health Admin user
    Then the changes should be saved successfully
