Feature: Patient Logs Add or Edit HbA1c

  Scenario: Doctor adds or edits HbA1c value in the Patient Logs tab
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the navigates Trend to Patient Logs
    And the doctor adds or edits the HbA1c value
    Then the updated HbA1c value should be saved and visible
