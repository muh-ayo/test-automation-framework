from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utils.logger import logger
import yaml
import os
from selenium.webdriver.chrome.service import Service

class BasePage:
    def __init__(self):
        # Load config with error handling
        try:
            with open('config/config.yaml', 'r') as file:
                config = yaml.safe_load(file)
        except FileNotFoundError:
            logger.error("config.yaml not found. Using default values.")
            config = {'environment': {'test': {'base_url': '', 'timeout': 10}}}
        
        self.env = os.getenv('ENV', 'test')
        self.timeout = config['environment'].get(self.env, {'timeout': 10})['timeout']
        
        # Set up ChromeDriver
        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
            logger.info("Initialized Chrome WebDriver")
        except Exception as e:
            logger.error(f"Failed to initialize WebDriver: {str(e)}")
            raise

        self.wait = WebDriverWait(self.driver, self.timeout)

    def find_element(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            logger.info(f"Found element with locator: {locator}")
            return element
        except Exception as e:
            logger.error(f"Element not found with locator: {locator}. Error: {str(e)}")
            raise
    
    def is_element_visible(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            logger.info(f"Found element with locator visible: {locator}")
            return element
        except Exception as e:
            logger.error(f"Element with locator not found to be visible : {locator}. Error: {str(e)}")
            raise
    
    
    def click(self, locator):
        try:
            self.find_element(locator).click()
            logger.info(f"Clicked element with locator: {locator}")
        except Exception as e:
            logger.error(f"Failed to click element with locator: {locator}. Error: {str(e)}")
            raise

    def type_text(self, locator, text):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            logger.info(f"Typed '{text}' into element with locator: {locator}")
        except Exception as e:
            logger.error(f"Failed to type into element with locator: {locator}. Error: {str(e)}")
            raise

    def get_text(self, locator):
        try:
            element = self.find_element(locator)
            element_text = element.text
            logger.info(f"Found'{element_text}' as a text in element with locator: {locator}")
            return element_text
        except Exception as e:
            logger.error(f"Failed to get text from element with locator: {locator}. Error: {str(e)}")
            raise

    def get_title(self):
        try:
            title = self.driver.title
            logger.info(f"Retrieved page title: {title}")
            return title
        except Exception as e:
            logger.error(f"Failed to get page title: {str(e)}")
            raise
    
    def get_url(self):
        try:
            url = self.driver.current_url
            logger.info(f"Retrieved url title: {url}")
            return url
        except Exception as e:
            logger.error(f"Failed to get url title: {str(e)}")
            raise

    def quit(self):
        try:
            self.driver.quit()
            logger.info("Closed WebDriver")
        except Exception as e:
            logger.error(f"Failed to close WebDriver: {str(e)}")
