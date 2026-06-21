Feature: refresh page

  Scenario: HPB Admin refreshes Clinic User page successfully
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the Fullerton Health page
    And selects doctor to view its doctors
    And selects fh to view its admins
    And the user refreshes the page
    Then the page should be refreshed successfully