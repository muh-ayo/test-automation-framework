from pages.login_page import LoginPage
from utils.logger import logger
from utils.test_data import TestData

def before_all(context):
    context.logger = logger
    context.test_data = TestData()
    logger.info("Initialized test environment")

def after_all(context):
    context.login_page = LoginPage()
    context.login_page.quit()
    logger.info("Cleaned up test environment")

def before_scenario(context, scenario):
    context.login_page = LoginPage()
    logger.info(f"Starting scenario: {scenario.name}")

def after_scenario(context, scenario):
    logger.info(f"Finished scenario: {scenario.name}")
