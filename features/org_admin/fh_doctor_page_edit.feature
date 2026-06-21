Feature: Edit Doctor from Fullerton Health Doctor Page

  Scenario: HPB Admin edits a doctor's profile from the Fullerton Health doctor list
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the Fullerton Health page
    And selects doctor to view its doctors
    And edits the information of doctor
    Then the updated details should appear in the doctor's profile