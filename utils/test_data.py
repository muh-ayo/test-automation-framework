import os
from dotenv import load_dotenv

load_dotenv()

class TestData:
    def __init__(self):
        # Load credentials from environment variables
        self.VALID_USERNAME = os.getenv('VALID_USERNAME', '')
        self.VALID_PASSWORD = os.getenv('VALID_PASSWORD', '')
        self.INVALID_USERNAME = os.getenv('INVALID_USERNAME', '')
        self.INVALID_PASSWORD = os.getenv('INVALID_PASSWORD', '')
        self.EMPTY_USERNAME = ""
        self.EMPTY_PASSWORD = ""
        self.error_message = "Invalid credentials"
        self.empty_username_error_message=  "Required"
        self.empty_password_error_message = "Required"