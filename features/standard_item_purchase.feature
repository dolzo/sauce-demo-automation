Feature: standard Item Purchase

@high
Scenario: Purchase an item with a regular user
    Given the user goes to the website
    When the user enters valid credentials for an standard user
    And the user adds an item to the cart
    And the user completes the checkout process
    Then the user is shown a thank you message for its order