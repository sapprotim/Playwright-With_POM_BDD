Feature: Uncheck permission checkbox
  Scenario: User unchecks a permission checkbox for a custom role
    Given the HPB Admin is logged in
    When the user navigates to the Role Manager page
    And the user creates a new custom role
    And the user deletes the custom role
    Then the custom role should be removed successfully