Feature: Clinic Doctor page access

  Scenario: Open and view the clinic doctor list
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the clinic page
    And selects doctor to view its doctors
    Then the list of assigned doctors should be displayed