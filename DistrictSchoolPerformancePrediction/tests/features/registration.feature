Feature: Registration

  Scenario: Account Creation
      Given I am on the Register page
       When I provide a Username, Email, Password, and Confirmation
       And I click Sign Up
       Then I should see "Your account has been created! You can now Login"
