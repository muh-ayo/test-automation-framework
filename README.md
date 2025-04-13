# Automation Test Framework for HMCTS Technical Test Submitted by Ibrahim Muhammed

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set and copy environment varaiblesto the root directory by using the .env file attached to the submission which can be retrieve from the submission attached to the email
3. Ensure Google Chrome is installed and updated

## Running Tests Locally
- All tests with terminal output: `behave features/`
- All tests with HTML report: `behave features/ -f behave_html_formatter:HTMLFormatter -o reports/behave-report.html`
- View the HTML report by opening `reports/behave-report.html` in a web browser (e.g., `open reports/behave-report.html` on Mac).


## Features
- POM and BDD combination
- Logging
- Error handling
- Jenkins CI/CD integration
- Visual HTML reporting
- Comprehensive login and logout testing

## CI/CD with Jenkins
- The `Jenkinsfile` defines the CI pipeline.
- To set up Jenkins:
  1. Install Jenkins on a server.
  2. Create a new pipeline job.
  3. Point it to the repository and use the `Jenkinsfile`.
  4. Trigger builds on code pushes (e.g. via a webhook).
- Tests run automatically when code is pushed to the repository.
- Logs are saved in `logs/test_logs.log`.
- HTML report is saved in `reports/behave-report.html` and archived in Jenkins (check build artifacts).

## Test Scenarios Coverage
### Login and Logout (`features/login.feature`)
- Successful login with valid credentials
- Successful logout after login
- Failed login with invalid username and valid password
- Failed login with invalid username and invalid password
- Failed login with empty username and valid password
- Failed login with valid username and empty password
- Failed login with empty username and empty password
- Failed login with valid username and invalid password

## Notes
- Do not change the `config.yaml` as the variables provided have been used for this technical test.
- Ensure Python 3.9 is installed on your machine
- If YAML errors occur, verify `config.yaml` syntax (2 spaces, no tabs).

## Explanation of Design Choice 
    I chose to pair both Page Object Model(POM) and Behavior Driven Design(BDD) as my design choice because the two approach complement eachother to achieve a scalable and organised automation framework which POM offers by organizing code in to specific pages which make it eay to mantain framework. 
    I have also used BDD so as to make communication clear and understandable between technical and non-technical team members. The BDD Gherkin syntax, like 'Given I am on the login page, When I enter a valid username' makes test scenarios readable and easy to maintain. It also aligns tests with business requirements. Overall the combination of POM and BDD make the solution robust and can be use to design any automation framework regardless of the size of the project.

##  Additional improvement
-   Parallel execution to make test run faster
-   Cross browser testing to run test on other browsers and not only chrome
-   Basic security testing like SQI Injection and cross site scripting
-   Performance
-   Headless mode options
-   Accesibility
-   Run test in a docker container
-   Retry Mechanism: Reduces flaky failures by retrying failed scenarios once.



 


