Feature: Doctor page view Access

  Scenario: Clinic Admin accesses the Doctor Admin page
    Given the Clinic Admin is logged in
    When the Admin selects the Doctor Admin role
    Then the Doctor Admin page is displayed