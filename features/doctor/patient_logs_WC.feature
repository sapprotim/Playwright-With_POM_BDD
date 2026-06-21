Feature: Patient Logs Waist Circumference add and edit

  Scenario: Doctor adds, edits and verify Waist Circumference data records in Patient Logs
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the navigates Trend to Patient Logs
    And the doctor adds and edits waist circumference
    Then the waist circumference value should be visible and matched with updated value
