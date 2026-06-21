Feature: Delete Clinic

  Scenario: HPB Admin deletes a clinic and verifies it is removed from the list
    Given the HPB Admin is logged in
    When selects a clinic to delete
    Then the clinic should no longer appear in the clinic list
