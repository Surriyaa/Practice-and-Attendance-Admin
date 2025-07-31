import csv
import logging

logger = logging.getLogger(__name__)

def load_questions_from_csv(path):
    logger.debug(f"Opening CSV file at path: {path}")
    with open(path, newline='') as csvfile:
        logger.debug("CSV file opened successfully")
        reader = csv.DictReader(csvfile)
        logger.debug("Initialized csv.DictReader")
        data = {"level1": [], "level2": [], "level3": []}
        logger.debug(f"Initialized data dictionary: {data}")
        for row in reader:
            logger.debug(f"Read row: {row}")
            if row["level1"]:
                logger.debug(f"Appending to level1: {row['level1']}")
                data["level1"].append(row["level1"])
            if row["level2"]:
                logger.debug(f"Appending to level2: {row['level2']}")
                data["level2"].append(row["level2"])
            if row["level3"]:
                logger.debug(f"Appending to level3: {row['level3']}")
                data["level3"].append(row["level3"])
        logger.debug(f"Final data collected: {data}")
    logger.debug("Returning data")
    return data