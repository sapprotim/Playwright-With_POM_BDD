Feature: HPB Admin Role Access

  Scenario: Open and view the HPB Admin user list
    Given the HPB Admin is logged in
    When selects the HPB Admin role
    Then the HPB Admin user list should be displayed