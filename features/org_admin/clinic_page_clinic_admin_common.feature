Feature: Clinic's Clinic Admin page access

  Scenario: Open and view the clinic's Clinic Admin list
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the clinic page
    And selects doctor to view its doctors
    And selects Clinic Admin to view its Clinic Admins
    Then the list of assigned Clinic Admin should be displayed