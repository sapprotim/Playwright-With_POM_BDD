Feature: Select user types

  Scenario: Fullerton Health Admin selects the "Prospects" and views the corresponding user page
    Given the fullerton health admin is logged in
    When selects the "Prospects" user
    Then the "Prospects" user page is displayed