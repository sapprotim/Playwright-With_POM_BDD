

Feature: Check permission checkbox
  Scenario: User checks a permission checkbox for a custom role
    Given the HPB Admin is logged in
    When the user navigates to the Role Manager page
    And the user creates a new custom role
    And the user checks a permission checkbox
    Then the checkboxin successfully