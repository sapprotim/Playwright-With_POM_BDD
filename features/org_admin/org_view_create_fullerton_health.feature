Feature: Create Fullerton Health

  Scenario: HPB Admin creates a new Fullerton Health
    Given the HPB Admin is logged in
    When admin creates a Fullerton Health
    Then the Fullerton Health should be created successfully