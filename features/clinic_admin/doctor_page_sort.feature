Feature: Table sorting

  Scenario: Clinic Admin sorts user names in ascending order on the Doctor Admin page
    Given the Clinic Admin is logged in
    When the Admin selects the Doctor Admin role
    And the user clicks the Name column to sort A-Z
    Then the table should reflect the sorted order accordingly
