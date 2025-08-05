import logging
import os
from datetime import datetime

class Logger:
    _log_file_created = False
    _log_file_path = None

    @staticmethod
    def get_logger(name):
        # Create logs directory if it doesn't exist
        log_dir = "C:/Users/ASUS/PycharmProjects/Practice-Attendance-Admin/logs"
        os.makedirs(log_dir, exist_ok=True)

        # Generate only one log file for the entire run
        if not Logger._log_file_created:
            Logger._log_file_path = os.path.join(
                log_dir, f"log_file_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
            )
            Logger._log_file_created = True

        # Setup logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # Avoid adding multiple handlers
        if not logger.handlers:
            # File Handler - common log file for whole session
            fh = logging.FileHandler(Logger._log_file_path)
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
