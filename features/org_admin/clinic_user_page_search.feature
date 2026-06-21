Feature: search

  Scenario: HPB Admin searches for a user by name in Clinic User's page and views matching results
   Given the HPB Admin is logged in
   When the HPB Admin navigates to the clinic page
   And searches for a name
   Then the system should display the matching user