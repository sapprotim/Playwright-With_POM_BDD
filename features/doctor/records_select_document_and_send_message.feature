Feature: Document sending with message

  Scenario: Doctor sends a document with a message from the Records page
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the Doctor Admin navigates to Records page
    And sends the document with a message
    Then the confirmation message 'Documents message sent to user successfully' should appear