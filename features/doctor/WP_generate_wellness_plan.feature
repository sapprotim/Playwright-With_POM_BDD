Feature: Generate Wellness Plan

  Scenario: Doctor generates a wellness plan for a user on the Wellness Plan page
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the Doctor Admin navigates to the WP page
    And clicks the 'Generate Wellness Plan' button
    Then the wellness plan should be generated successfully