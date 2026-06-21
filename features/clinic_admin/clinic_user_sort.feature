Feature: Table sorting

  Scenario: Clinic Admin sorts user names in ascending or descending order
    Given the Clinic Admin is logged in
    When the admin clicks the headers column to sort
    Then the system should display result in ascending/descending order
