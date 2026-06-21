Feature: Assign Clinic Admin to Clinic Admin page

  Scenario: HPB Admin assigns a Admin to a Clinic Admin page
    Given the HPB Admin is logged in
    When the HPB Admin navigates to the clinic page
    And selects Clinic Admin to view its Clinic Admins
    And selects doctor to view its doctors
    And clicks the 'Assign Clinic Admin' button
    Then the Clinic Admin should be listed under the assigned Clinic Admin page
