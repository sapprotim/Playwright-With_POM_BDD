Feature: Filter functionality for Clinic user

  Scenario: Clinic Admin applies filters and views filtered results
    Given the Clinic Admin is logged in
    When the admin applies the filter
    Then the system should display filtered results matching selected criteria