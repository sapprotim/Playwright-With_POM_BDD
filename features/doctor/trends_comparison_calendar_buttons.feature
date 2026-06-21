Feature: View filter and Calendar buttons

  Scenario: Verify that filter buttons are visible and clickable
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And navigates to the Lifestyle tab
    And the admin clicks View filter and Calendar
    Then the filter and Calendar buttons should be visible
