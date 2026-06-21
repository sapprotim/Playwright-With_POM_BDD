Feature: Edit Clinic Admin from Clinic's Clinic Admin Page

  Scenario: HPB Admin edits an admin's profile from the clinic's clinic admin list
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the clinic page
    And selects doctor to view its doctors
    And selects Clinic Admin to view its Clinic Admins
    And edits the information of clinic admin
    Then the updated details should appear in the clinic admin's profile
