import logging
import os
from datetime import datetime

class Logger:
    @staticmethod
    def get_logger(name):
        # Create logs directory if it doesn't exist
        log_dir = "C:/Users/ASUS/PycharmProjects/Practice-Attendance-Admin/logs"
        os.makedirs(log_dir, exist_ok=True)

        # Generate log file name with timestamp
        log_file = os.path.join(log_dir, f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log")

        # Setup logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # Avoid adding multiple handlers if logger already has them
        if not logger.handlers:
            # File Handler
            fh = logging.FileHandler(log_file)
            fh.setLevel(logging.DEBUG)

            # Console Handler
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # Formatter
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # Add handlers
            logger.addHandler(fh)
            logger.addHandler(ch)

        return logger
