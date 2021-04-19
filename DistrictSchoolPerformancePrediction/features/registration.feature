@in_progress
Feature: Registration

  Scenario: Account Creation
      Given I am on the "Register" page
      And I have my registration information
    | username | email            | password1 | password2
    | test123  | test123@test.com | pw123     | pw123
       When I provide a <username>, <email>, <password1>, and <password2>
       And I click Sign Up
       Then I should see "Your account has been created! You can now Login"
