Feature: search

  Scenario: HPB Admin searches for a user by name in HPB Admin page and views matching results
    Given the HPB Admin is logged in
    When selects the HPB Admin role
   And the HPB admin searches for a name
   Then the system should display the matching user





