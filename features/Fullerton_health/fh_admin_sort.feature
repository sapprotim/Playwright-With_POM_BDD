Feature: Sorting Control

  Scenario: FH Admin selects the Fullerton Health Admin page and sorts the table by Name A-Z and verifies the sorted order
   Given the fullerton health admin is logged in
   When the Admin selects the Fullerton Health Admin role
   And the user clicks the Name column to sort A-Z
   Then the table should reflect the sorted order accordingly





