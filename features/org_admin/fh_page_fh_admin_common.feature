Feature: Fullerton Health User page access

  Scenario: Open and view the HPB Admin user list
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the Fullerton Health page
    And selects doctor to view its doctors
    And selects fh to view its admins
    Then the list of assigned admins should be displayed