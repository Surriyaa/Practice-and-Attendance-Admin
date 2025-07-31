import openpyxl

# Setup logger
from com.bridgelabz.utilities.logger import Logger
logger = Logger.get_logger("QuestionLoader")

def load_questions_from_excel(file_path):
    logger.info(f"Loading Excel file: {file_path}")
    workbook = openpyxl.load_workbook(file_path)
    data = {}

    for sheet in workbook.sheetnames:
        logger.info(f"Reading sheet: {sheet}")
        worksheet = workbook[sheet]
        questions = []
        for row in worksheet.iter_rows(min_row=2, max_col=1, values_only=True):
            question = row[0]
            if question:
                logger.debug(f"Found question in {sheet}: {question}")
                questions.append(question)
        data[sheet.lower()] = questions  # e.g., "Level1" → "level1"

    logger.info("Finished loading all levels")
    return data
