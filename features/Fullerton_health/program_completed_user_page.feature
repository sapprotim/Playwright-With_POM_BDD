Feature: Programme Completed User Tabs in Admin Panel

  Scenario: Fullerton Health Admin Navigate to Programme Completed Users
    Given the fullerton health admin is logged in
    When the Admin opens the Users page
    And the user selects the Programme Completed Users tab
    Then the Programme Completed Users tab should be displayed