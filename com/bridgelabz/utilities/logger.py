# utilities/logger.py
import logging
import os
from datetime import datetime

class Logger:
    _log_file_created = False
    _log_file_path = None

    @staticmethod
    def get_logger(name, tc_id=None):
        log_dir = "C:/Users/ASUS/PycharmProjects/Practice-Attendance-Admin/logs"
        os.makedirs(log_dir, exist_ok=True)

        if not Logger._log_file_created:
            Logger._log_file_path = os.path.join(
                log_dir, f"log_file_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
            )
            Logger._log_file_created = True

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            fh = logging.FileHandler(Logger._log_file_path)
            fh.setLevel(logging.DEBUG)

            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            formatter = logging.Formatter(
                '[%(tc_id)s] - %(asctime)s - %(levelname)s - %(name)s - %(message)s'
            )
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            logger.addHandler(fh)
            logger.addHandler(ch)

        return logging.LoggerAdapter(logger, {'tc_id': tc_id if tc_id else 'TC_01'})
