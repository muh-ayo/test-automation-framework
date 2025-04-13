Feature: User Login and Authentication
  As a registered user
  I want to log in and out of the application securely
  So that I can access my account and ensure only authorised users log in

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter valid username
    And I enter valid password
    And I click the login button
    Then I should see the dashboard page

  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter invalid username
    And I enter invalid password
    And I click the login button
    Then I should see an error message

  Scenario: Failed login with invalid username and valid password
    Given I am on the login page
    When I enter invalid username
    And I enter valid password
    And I click the login button
    Then I should see an error message
  
  Scenario: Failed login with valid username and invalid password
    Given I am on the login page
    When I enter valid username
    And I enter invalid password
    And I click the login button
    Then I should see an error message

  Scenario: Failed login with empty username and valid password
    Given I am on the login page
    When I enter empty username
    And I enter valid password
    And I click the login button
    Then I should see username required error message
  
  Scenario: Failed login with valid username and empty password
    Given I am on the login page
    When I enter valid username
    And I enter empty password
    And I click the login button
    Then I should see password required error message

  Scenario: Failed login with empty username and empty password
    Given I am on the login page
    When I enter empty username
    And I enter empty password
    And I click the login button
    Then I should see username required error message

  Scenario: Successful user logout
    Given I am on the login page
    When I enter valid username
    And I enter valid password
    And I click the login button
    Then I should see the dashboard page
    When I click on the menu button
    And I click on the logout button
    Then I return back to the login page
  