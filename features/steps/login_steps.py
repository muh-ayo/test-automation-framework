import time
from behave import given, when, then
from utils.logger import logger
from utils.test_data import TestData

@given('I am on the login page')
def step_open_login_page(context):
    try:
        context.login_page.open()
        context.logger.info("Opened login page successfully")
    except Exception as e:
        context.logger.error(f"Failed to open login page: {str(e)}")
        raise

@when('I enter valid username')
def step_enter_valid_username(context):
    try:
        context.login_page.enter_username(context.test_data.VALID_USERNAME)
        context.logger.info(f"Entered valid username: {context.test_data.VALID_USERNAME}")
    except Exception as e:
        context.logger.error(f"Failed to enter valid username: {str(e)}")
        raise

@when('I enter valid password')
def step_enter_valid_password(context):
    try:
        context.login_page.enter_password(context.test_data.VALID_PASSWORD)
        context.logger.info("Entered valid password")
    except Exception as e:
        context.logger.error(f"Failed to enter valid password: {str(e)}")
        raise

@when('I enter invalid username')
def step_enter_invalid_username(context):
    try:
        context.login_page.enter_username(context.test_data.INVALID_USERNAME)
        context.logger.info(f"Entered invalid username: {context.test_data.INVALID_USERNAME}")
    except Exception as e:
        context.logger.error(f"Failed to enter invalid username: {str(e)}")
        raise

@when('I enter invalid password')
def step_enter_invalid_password(context):
    try:
        context.login_page.enter_password(context.test_data.INVALID_PASSWORD)
        context.logger.info("Entered invalid password")
    except Exception as e:
        context.logger.error(f"Failed to enter invalid password: {str(e)}")
        raise

@when('I enter empty username')
def step_enter_empty_username(context):
    try:
        context.login_page.enter_username("")
        context.logger.info(f"Entered empty username: {""}")
    except Exception as e:
        context.logger.error(f"Failed to enter empty username: {str(e)}")
        raise

@when('I enter empty password')
def step_enter_empty_password(context):
    try:
        context.login_page.enter_password("")
        context.logger.info("Entered empty password")
    except Exception as e:
        context.logger.error(f"Failed to enter empty password: {str(e)}")
        raise

@when('I click the login button')
def step_click_login(context):
    try:
        context.login_page.click_login()
        context.logger.info("Clicked login button")
    except Exception as e:
        context.logger.error(f"Failed to click login button: {str(e)}")
        raise

@when('I click on the menu button')
def step_click_menu(context):
    try:
        context.login_page.click_menu()
        context.logger.info("Clicked menu button")
    except Exception as e:
        context.logger.error(f"Failed to click menu button: {str(e)}")
        raise

@when('I click on the logout button')
def step_click_logout(context):
    try:
        context.login_page.click_logout()
        context.logger.info("Clicked logout button")
    except Exception as e:
        context.logger.error(f"Failed to click logout button: {str(e)}")
        raise

@then('I should see the dashboard page')
def step_verify_dashboard(context):
    try:
        time.sleep(3)
        assert "dashboard/index" in context.login_page.get_url(), "dashboard/index not found in url"
        msg = context.login_page.check_dashboard_text()
        assert msg == 'Dashboard', f"Dashboard text not found, found, '{msg}'"
        context.logger.info("Verified user login to dasboard page")
    except AssertionError as e:
        context.logger.error(f"Dashboard page verification failed: {str(e)}")
        raise
    

@then('I should see an error message')
def step_verify_error_message(context):
    try:
        error_msg = context.login_page.get_error_message()
        assert error_msg == context.test_data.error_message, f"Expected error message '{context.test_data.error_message}', got '{error_msg}'"
        context.logger.info(f"Verified error message: {context.test_data.error_message}")
    except AssertionError as e:
        context.logger.error(f"Error message verification failed: {str(e)}")
        raise
    

@then('I should see username required error message')
def step_verify_username_required_error_message(context):
    try:
        error_msg = context.login_page.get_empty_field_error_message()
        assert context.test_data.empty_username_error_message in error_msg, f"Expected error message '{context.test_data.empty_username_error_message}', got '{error_msg}'"
        context.logger.info(f"Verified error message: {context.test_data.empty_username_error_message}")
    except AssertionError as e:
        context.logger.error(f"Error message verification failed: {str(e)}")
        raise
    

@then('I should see password required error message')
def step_verify_password_required_error_message(context):
    try:
        error_msg = context.login_page.get_empty_field_error_message()
        assert context.test_data.empty_password_error_message in error_msg, f"Expected error message '{context.test_data.empty_password_error_message}', got '{error_msg}'"
        context.logger.info(f"Verified error message: {context.test_data.empty_password_error_message}")
    except AssertionError as e:
        context.logger.error(f"Error message verification failed: {str(e)}")
        raise
    

@then('I return back to the login page')
def step_verify_user_return_to_logon(context):
    try:
        assert context.login_page.get_url() == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login" , "user not return to login page"
        context.login_page.check_visible_after_logout() 
        context.logger.info("User back to login page")
    except AssertionError as e:
        context.logger.error(f"logout failed: {str(e)}")
        raise