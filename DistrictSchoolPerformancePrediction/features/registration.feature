Feature: Registration

  Scenario: Account Creation
      Given I am on the "Register" page
      When I provide a <username>, <email>, <password1>, and <password2>
      | username | email            | password1 | password2 |
      | test123  | test123@test.com | PWTSB4321 | PWTSB4321 |
      And I click "Sign Up"
      Then I should see "Your account has been created! You can now Login"
