Feature: Pagination Control

  Scenario: Doctor changes the page size and verifies table updates accordingly
    Given the doctor Admin is logged in
    When the user selects different page sizes
    Then the table should reflect the selected page size




