Feature: Upload

  Background: Register and Login

  Scenario: Upload a CSV file
      Given I am on the "Upload" page
       When I click Choose File
       And I select a CSV to upload
       And I click Upload
       Then I should see a confirmation message that the upload was successful