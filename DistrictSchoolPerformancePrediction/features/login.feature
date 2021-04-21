Feature: Login

  Background: Register
    Given I am on the "Login" page

  Scenario: Log in to website
       When I enter my <username>, <password>
       | username | password |
       | testuser | TestPW123|
       And I click Login
       Then I should see "Upload File"
       And I should not see "Register"