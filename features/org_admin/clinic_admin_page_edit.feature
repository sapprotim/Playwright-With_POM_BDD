Feature: Edit Clinic Admin Details

  Scenario: Successfully edit the clinic admin information
    Given the HPB Admin is logged in
    When selects the Clinic Admin role
    And Edit the clinic admin details
    Then Clinic admin should be updated successfully