Feature: standard Login

@high
Scenario: Log in into the page with a regular user
    Given the user goes to the website
    When the user enters valid credentials
    Then the user is redirected to the main page with its account
