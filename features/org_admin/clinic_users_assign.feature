Feature: Assign Users to Clinic

  Scenario: HPB Admin assigns a user to a clinic
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the clinic page
    And clicks the 'Assign Users' button
    Then the user should be listed under the assigned clinic
