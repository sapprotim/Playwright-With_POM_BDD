Feature: Patient Logs Blood Pressure input and validate data

  Scenario: Doctor inputs a blood pressure records in Patient Logs and validate data
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the navigates Trend to Patient Logs
    And the blood pressure section should be able to input data
    Then blood pressure readings should be listed and matches with the inputted data
