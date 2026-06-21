Feature: All User Tabs in Admin Panel

  Scenario: Select All Users tab
    Given the HPB Admin is logged in
    When the Admin opens the Users page
    And the user selects the All Users tab
    Then the All Users tab should be displayed