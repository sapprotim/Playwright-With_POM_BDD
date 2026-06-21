Feature: Delete Fullerton Health

  Scenario: HPB Admin deletes a Fullerton Health and verifies it is removed from the list
    Given the HPB Admin is logged in
    When selects a Fullerton Health to delete
    Then the Fullerton Health should no longer appear in the Fullerton Health list