Feature: Clinic Admin Access

  Scenario: Fullerton Health Admin selects Clinic Admin role and views the Clinic Admin page
    Given the fullerton health admin is logged in
    When selects the Clinic Admin role
    Then the Clinic Admin page is displayed