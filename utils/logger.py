import logging
import os

class TestLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Try to write to file
        try:
            if not os.path.exists('logs'):
                os.makedirs('logs')
            file_handler = logging.FileHandler('logs/test_logs.log')
            file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            self.logger.addHandler(file_handler)
        except Exception as e:
            print(f"Failed to set up file logging: {e}")
            # Fallback to console
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

logger = TestLogger()