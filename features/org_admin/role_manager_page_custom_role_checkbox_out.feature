Feature: Uncheck permission checkbox
  Scenario: User unchecks a permission checkbox for a custom role
    Given the HPB Admin is logged in
    When the user navigates to the Role Manager page
    And the user creates a new custom role
    And the user unchecks the permission checkbox
    Then the checkboxout successfully