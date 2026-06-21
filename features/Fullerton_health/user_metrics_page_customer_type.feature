Feature: Customer Type Selection

  Scenario: Fullerton Health Admin selects all customer types one by one, ending with "Public" as the final selection
    Given the fullerton health admin is logged in
    When the Admin opens the User Metrics page
    And the user selects all customer types one by one
    Then the last selected customer type should be Public