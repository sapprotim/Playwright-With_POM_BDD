Feature: Zendesk user Page Access

  Scenario: Fullerton Health Admin opens Zendesk user Page
    Given the fullerton health admin is logged in
    When the Admin opens the Zendesk Users page
    Then the Zendesk Users page should be displayed