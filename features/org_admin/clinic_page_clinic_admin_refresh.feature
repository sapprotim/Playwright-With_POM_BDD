Feature: refresh page

  Scenario: HPB Admin refreshes Clinic's Clinic Admin page successfully
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the clinic page
    And selects doctor to view its doctors
    And selects Clinic Admin to view its Clinic Admins
    And the user refreshes the page
    Then the page should be refreshed successfully