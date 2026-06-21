Feature: Edit Doctor from Clinic Doctor Page

  Scenario: HPB Admin edits a doctor's profile from the clinic doctor list
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the clinic page
    And selects doctor to view its doctors
    And edits the information of doctor
    Then the updated details should appear in the doctor's profile