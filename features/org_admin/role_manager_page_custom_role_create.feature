Feature: Role Manager Navigation

  Scenario: Navigate to Role Manager page
    Given the HPB Admin is logged in
    When the user navigates to the Role Manager page
    And the user creates a new custom role
    Then the custom role create successfully

