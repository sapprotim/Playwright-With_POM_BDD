Feature: Post Programme Survey

  Scenario: Fullerton Health Admin sends Post Programme Survey to Doctor
    Given the fullerton health admin is logged in
    When the Admin selects the Doctor Admin role
    And sends a Post Programme Survey to the doctor
    Then the survey should be recorded with the correct sent date
