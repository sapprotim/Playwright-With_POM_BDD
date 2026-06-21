Feature: Patient Logs Weight and BMI add and edit

  Scenario: Doctor adds, edits and verify Weight and BMI data records in Patient Logs
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the navigates Trend to Patient Logs
    And the doctor adds and edits weight and BMI
    Then the values of weight and BMI should be matched with the updated values
