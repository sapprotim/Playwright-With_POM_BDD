Feature: search

  Scenario: Fullerton Health Admin searches for a user under "Zendesk Users page" and views matching results
   Given the fullerton health admin is logged in
   When the Admin opens the Zendesk Users page
   And the zendesk user searches for a name
   Then the system should display the matching user