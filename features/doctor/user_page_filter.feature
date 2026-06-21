Feature: Doctor user page filtering

  Scenario: Doctor filters users by clinic and verifies the displayed results
    Given the doctor Admin is logged in
    When the doctor filters users by clinic
    Then the filtered result should be displayed correctly