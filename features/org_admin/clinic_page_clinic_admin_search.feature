Feature: search

  Scenario: HPB Admin searches for an Admin by name in Clinic's Clinic Admin page and views matching results
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the clinic page
    And selects doctor to view its doctors
    And selects Clinic Admin to view its Clinic Admins
   And the Clinic Admin searches for a Clinic Admin
   Then the system should display the matching user