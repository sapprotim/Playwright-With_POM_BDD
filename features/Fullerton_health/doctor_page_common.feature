Feature: Doctor page view Access

  Scenario: Fullerton Health Admin selects Doctor to open and view the Doctor page tab
    Given the fullerton health admin is logged in
    When the Admin selects the Doctor Admin role
    Then the Doctor Admin page is displayed