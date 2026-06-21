Feature: Doctor Account Creation

  Scenario: Successfully create a new Doctor account
    Given the HPB Admin is logged in
    When the Admin selects the Doctor Admin role
    And edits the information of doctor
    Then the updated details should appear in the doctor's profile


