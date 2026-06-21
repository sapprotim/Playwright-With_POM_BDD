Feature: search

  Scenario: Fullerton Health Admin searches for a doctor by name in Doctor page and views matching results
   Given the HPB Admin is logged in
   When the Admin selects the Doctor Admin role
   And the doctor searches for a name
   Then the system should display the matching user





