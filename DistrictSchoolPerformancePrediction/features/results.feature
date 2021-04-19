@in_progress
Feature: Results

Background: Register, Login, Upload

  Scenario: See results from ML predictions
      Given I am on the Results page
      Then I should see the processed CSV data
      
  Scenario: Download ML predictions
      Given I am on the Results page
      When I click the Download CSV button
      Then I should download a CSV of ML predictions