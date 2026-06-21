Feature: Invite Users Tab
  Scenario: Fullerton Health Admin Navigate to Invited Users
    Given the HPB Admin is logged in
    When the Admin opens the Users page
    And the user selects the Invited Users tab
    Then the Invited Users tab should be displayed