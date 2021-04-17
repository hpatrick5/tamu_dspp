Feature: Login

  Background: Register

  Scenario: Log in to website
      Given I am on the Login page
       When I enter my Username, Password
       And I click Login
       Then I should see Upload File
       And I should not see Register