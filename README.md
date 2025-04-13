# Automation Test Framework for HMCTS Technical Test Submitted by Ibrahim Muhammed

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set and copy environment varaiblesto the root directory by using the .env file attached to the submission which can be retrieve from the submission attached to the email

## Running Tests Locally
- All tests without hmtl behave report : `behave features/`
- All tests with html behave report:  `behave features/ -f behave_html_formatter:HTMLFormatter -o reports/behave-report.html`


## Features
- POM and BDD combination
- Logging
- Error handling


## Notes
- DO not change the `config.yaml` as the variables provided have been used for this technical test.
- Ensure Python 3.9 is installed on your machine
- If YAML errors occur, verify `config.yaml` syntax (2 spaces, no tabs).