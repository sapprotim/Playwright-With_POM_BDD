Feature: sorting

  Scenario: Clinic Admin sorts user names in ascending order
    Given the Clinic Admin is logged in
    When selects the Clinic Admin role
    And the user clicks the Name column to sort A-Z
    Then the table should reflect the sorted order accordingly
