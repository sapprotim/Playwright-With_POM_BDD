Feature: Patient Logs Lipids entry

  Scenario: Doctor adds, edits and verify lipids data records in Patient Logs
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the navigates Trend to Patient Logs
    And the doctor adds and edits lipid values: Total Cholesterol, HDL, LDL, Triglycerides
    Then the lipids values should be visible and matched with updated value: Total Cholesterol, HDL, LDL, Triglycerides
