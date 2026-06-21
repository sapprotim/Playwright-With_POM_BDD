Feature: Reset sorting functionality

  Scenario: Clinic Admin resets the sorted list to default order
    Given the Clinic Admin is logged in
    When the user clicks on reset sort
    Then the system should reset the sort
