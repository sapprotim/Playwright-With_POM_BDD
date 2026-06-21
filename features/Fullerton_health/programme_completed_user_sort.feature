Feature: Sorting Control

  Scenario: FH Admin navigates to the Programme Completed User page and sorts the table by ascending/descending order and verifies the sorted order
   Given the fullerton health admin is logged in
   When the Admin opens the Users page
    And the user selects the Programme Completed Users tab
   And the admin clicks the headers column to sort
   Then the system should display result in ascending/descending order





