Feature: Delete Fullerton Health Admin

  Scenario: Delete a Fullerton Health Admin user
    Given the HPB Admin is logged in
    When the Admin selects the Fullerton Health Admin role
    And Add a new Fullerton Health Admin user
    And the user deletes a Fullerton Health Admin
    Then a successful deletion message should be shown



