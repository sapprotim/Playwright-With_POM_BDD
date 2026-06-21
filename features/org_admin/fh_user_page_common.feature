Feature: Fullerton Health User page access

  Scenario: Open and view the HPB Admin user list
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the Fullerton Health page
    Then the Fullerton Health user list should be displayed