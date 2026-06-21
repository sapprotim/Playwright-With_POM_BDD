Feature: Re-invite user
  Scenario: Re-inviting an invited user
    Given the fullerton health admin is logged in
    When the Admin opens the Users page
    And the user selects the Invited Users tab
    And resends the invite
    Then the Re_Invitation has been resent successfully





