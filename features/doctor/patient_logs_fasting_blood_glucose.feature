Feature: Patient Logs Fasting Blood Glucose input

  Scenario: Doctor inputs a fasting blood glucose records in Patient Logs
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the navigates Trend to Patient Logs
    And the doctor inputs a fasting blood glucose value
    Then the entered fasting blood glucose value should be saved and visible
