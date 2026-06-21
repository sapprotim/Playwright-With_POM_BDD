Feature: Withdrawn User Tabs in Admin Panel
  Scenario: Fullerton Health Admin Navigate to Withdrawn Users
    Given the fullerton health admin is logged in
    When the Admin opens the Users page
    And the user selects the Withdrawn Users tab
    Then the Withdrawn Users tab should be displayed