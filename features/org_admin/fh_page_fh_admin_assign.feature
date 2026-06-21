Feature: search

  Scenario: HPB Admin searches for a user by name in FH Admin's page and views matching results
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the Fullerton Health page
    And selects doctor to view its doctors
    And selects fh to view its admins
   And clicks the 'Assign Fullerton Health Admin' button
   Then the FH Admin should be listed under the assigned FH Admin page