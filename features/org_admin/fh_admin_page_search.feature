Feature: search

  Scenario: Fullerton Health Admin searches for a user by name in Fullerton Health Admin page and views matching results
   Given the HPB Admin is logged in
   When the Admin selects the Fullerton Health Admin role
   And the FH admin searches for a name
   Then the system should display the matching user




