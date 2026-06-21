Feature: Pagination Control

  Scenario: Fullerton Health Admin selects Clinic Admin, changes the page size and verifies table updates accordingly
    Given the fullerton health admin is logged in
    When selects the Clinic Admin role
    And the user selects different page sizes
    Then the table should reflect the selected page size