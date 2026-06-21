Feature: search

  Scenario: HPB Admin searches for a user by name in Clinic Admin page and views matching results
   Given the HPB Admin is logged in
   When selects the Clinic Admin role
   And the clinic searches for a name
   Then the system should display the matching user





