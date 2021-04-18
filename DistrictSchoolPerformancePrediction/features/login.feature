Feature: Login

  Background: Register
    Given: My account information
    | username | password |
    | test123  | pw123    |

  Scenario: Log in to website
      Given I am on the "Login" page
       When I enter my <username>, <password>
       And I click Login
       Then I should see "Upload File"
       And I should not see "Register"