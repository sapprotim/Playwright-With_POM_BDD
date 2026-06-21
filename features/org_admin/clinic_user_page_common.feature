Feature: Clinic User page access

  Scenario: Open and view the HPB Admin user list
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the clinic page
    Then the clinic user list should be displayed