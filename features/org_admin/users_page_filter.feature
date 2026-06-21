Feature: Filter functionality

  Scenario: Fullerton Health Admin filters on the Users Lists page and views the correct filtered results
    Given the HPB Admin is logged in
    When the Admin opens the Users page
    And the fh filters for users
    Then the fh filtered users should be displayed correctly









