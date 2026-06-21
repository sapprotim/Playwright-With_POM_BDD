Feature: Navigate Fullerton Health Admin page

  Scenario: Create a Fullerton Health Admin user
    Given the HPB Admin is logged in
    When the Admin selects the Fullerton Health Admin role
    And Add a new Fullerton Health Admin user
    Then the Fullerton Health Admin should be created successfully