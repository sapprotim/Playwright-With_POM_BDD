Feature: Pagination Control

  Scenario: HPB Admin selects Clinic's Clinic Admin page, changes the page size and verifies table updates accordingly
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the clinic page
    And selects doctor to view its doctors
    And selects Clinic Admin to view its Clinic Admins
    And the user selects different page sizes
    Then the table should reflect the selected page size