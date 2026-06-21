Feature: Uploads document

  Scenario: Doctor uploads a document to the Records page and views it successfully
    Given the doctor Admin is logged in
    When the doctor searches for a user profile
    And the Doctor Admin navigates to Records page
    And uploads a document
    Then the uploaded document should be visible in the records







