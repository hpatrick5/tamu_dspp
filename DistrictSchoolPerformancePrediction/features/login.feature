Feature: Login

  Background: Register
    Given I am registered
     | username | password    |
     | test123  | password123 |
    Given I am on the "Login" page

  Scenario: Log in to website
       When I enter my <username>, <password>
       And I click Login
       Then I should see "Upload File"
       And I should not see "Register"