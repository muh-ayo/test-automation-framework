from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import yaml
from utils.logger import logger
from .locators import Locators

class LoginPage(BasePage):
    USERNAME_FIELD = (By.XPATH, Locators.USERNAME_FIELD)
    PASSWORD_FIELD = (By.XPATH, Locators.PASSWORD_FIELD)
    LOGIN_BUTTON = (By.XPATH, Locators.LOGIN_BUTTON)
    ERROR_MESSAGE = (By.XPATH, Locators.ERROR_MESSAGE_FIELD)
    MENU_BUTTON = (By.XPATH, Locators.MENU_BUTTON)
    LOGOUT_BUTTON = (By.XPATH, Locators.LOGOUT_BUTTON)
    EMPTY_FIELD_ERROR = (By.XPATH, Locators.EMPTY_ERROR_FIELD)
    DASHBOARD_TEXT_FIELD = (By.XPATH, Locators.DASH_TEXT_FIELD)

    def __init__(self):
        super().__init__()
        try:
            with open('config/config.yaml', 'r') as file:
                config = yaml.safe_load(file)
        except FileNotFoundError:
            logger.error("config.yaml not found. Using default URL.")
            config = {'environment': {'test': {'base_url': 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'}}}
        
        self.url = f"{config['environment'].get(self.env, {'base_url': 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'})['base_url']}"

    def open(self):
        try:
            self.driver.get(self.url)
            logger.info(f"Opened URL: {self.url}")
            return self
        except Exception as e:
            logger.error(f"Failed to open URL {self.url}: {str(e)}")
            raise

    def enter_username(self, username):
        self.type_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.type_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def click_menu(self):
        self.click(self.MENU_BUTTON)

    def click_logout(self):
        self.is_element_visible(self.LOGOUT_BUTTON)
        self.click(self.LOGOUT_BUTTON)

        # self.is_element_visible(self.LOGOUT_BUTTON)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.LOGOUT_BUTTON)

      

        # self.driver.execute_script("argument[0].click();",self.LOGOUT_BUTTON)
        # self.click(self.LOGOUT_BUTTON)

    def check_visible_after_logout(self):
        self.is_element_visible(self.LOGIN_BUTTON)

    def check_dashboard_text(self):
        text = self.get_text(self.DASHBOARD_TEXT_FIELD)
        return text
    def get_error_message(self):
        try:
            message = self.find_element(self.ERROR_MESSAGE).text
            logger.info(f"Retrieved error message: {message}")
            return message
        except Exception as e:
            logger.error(f"Failed to get error message: {str(e)}")
            return ""
    
    def get_empty_field_error_message(self):
        try:
            message = self.find_element(self.EMPTY_FIELD_ERROR).text
            logger.info(f"Retrieved error message: {message}")
            return message
        except Exception as e:
            logger.error(f"Failed to get error message: {str(e)}")
            return ""
