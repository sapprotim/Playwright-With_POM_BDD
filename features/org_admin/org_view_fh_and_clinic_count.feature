Feature: View total Fullerton Health and clinic

  Scenario: HPB Admin views the total number of Fullerton Health and clinic
    Given the HPB Admin is logged in
    When clicks on the total in org view page
    Then the total number of Fullerton Health and Clinic should be displayed