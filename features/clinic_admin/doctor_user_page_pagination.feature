Feature: Pagination Control

  Scenario: Clinic Admin changes page size on the doctor user’s page
    Given the Clinic Admin is logged in
    When the Admin selects the Doctor Admin role
    And the Admin selects a doctor user
    And the user selects different page sizes
    Then the table should reflect the selected page size




