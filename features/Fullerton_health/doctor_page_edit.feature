Feature: Doctor Edit

  Scenario: Fullerton Health Admin edits a doctor's information
    Given the fullerton health admin is logged in
    When the Admin selects the Doctor Admin role
    And edits the information of doctor
    Then the updated details should appear in the doctor's profile