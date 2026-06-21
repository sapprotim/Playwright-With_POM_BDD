Feature: Doctor User Page View

  Scenario: Fullerton Health Admin selects Doctor, chooses a doctor user, and views the doctor user page
    Given the fullerton health admin is logged in
    When the Admin selects the Doctor Admin role
    And the Admin selects a doctor user
    Then the doctor user page is displayed