Feature: Pagination Control

  Scenario: HPB Admin navigates to Clinic user's page, changes the page size and verifies table updates accordingly
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the clinic page
    And the user selects different page sizes
    Then the table should reflect the selected page size
