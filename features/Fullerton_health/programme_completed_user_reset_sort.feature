Feature: Reset Sorting Control

  Scenario: FH Admin navigates to the Programme Completed User page and resets sorted table and verifies the sorted order
   Given the fullerton health admin is logged in
   When the Admin opens the Users page
    And the user selects the Programme Completed Users tab
   And the user clicks on reset sort
   Then the system should reset the sort





