from time import sleep
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MakerModule:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.driver = driver
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)

    # Locators
    maker_module_button_xpath = "//span[normalize-space()='Maker Module']"
    create_module_button_xpath = "//button[normalize-space()='CREATE MODULE']"
    select_module_dropdown_xpath = "//select[@name='module']"
    topic_input_xpath = "//input[@name='topic']"
    notes_input_xpath = "//input[@name='notes']"
    level1_input_xpath = "//input[@name='level1']"
    level2_input_xpath = "//input[@name='level2']"
    level3_input_xpath = "//input[@name='level3']"
    submit_button_xpath = "//button[normalize-space()='Submit']"
    save_button_xpath = "//button[normalize-space()='Save']"
    edit_icon_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[6]/button[1]/*[name()='svg'][1]"
    add_questions_button_xpath = "/html[1]/body[1]/div[3]/div[3]/button[1]/*[name()='svg'][1]"
    level1_questions_add_xpath = "//tbody/tr[3]/td[3]/span[1]"
    level2_questions_add_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[4]/span[1]"
    level3_questions_add_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[5]/span[1]"
    input_frame_xpath = "//div[@role='textbox']"
    disable_button_xpath="/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[6]/td[6]/button[2]"

    # Actions
    def click_maker_module(self):
        self.logger.debug("Clicking Maker Module button.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.maker_module_button_xpath))
        ).click()
        self.logger.debug("Clicked Maker Module button.")

    def click_create_module(self):
        self.logger.debug("Clicking Create Module button.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.create_module_button_xpath))
        ).click()
        self.logger.debug("Clicked Create Module button.")

    def select_module_dropdown(self, value):
        self.logger.debug("Selecting module dropdown with value: %s", value)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.select_module_dropdown_xpath))
        )
        drop = Select(self.driver.find_element(By.XPATH, self.select_module_dropdown_xpath))
        drop.select_by_value(str(value))
        self.logger.debug("Selected module dropdown with value: %s", value)

    def fill_module_form(self, topic, notes, level1, level2, level3):
        self.logger.debug("Filling module form with the given details.")
        self.driver.find_element(By.XPATH, self.topic_input_xpath).send_keys(topic)
        self.driver.find_element(By.XPATH, self.notes_input_xpath).send_keys(notes)
        self.driver.find_element(By.XPATH, self.level1_input_xpath).send_keys(level1)
        self.driver.find_element(By.XPATH, self.level2_input_xpath).send_keys(level2)
        self.driver.find_element(By.XPATH, self.level3_input_xpath).send_keys(level3)
        self.logger.debug("Filled module form.")

    def click_submit(self):
        self.logger.debug("Clicking Submit button.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.submit_button_xpath))
        ).click()
        self.logger.debug("Clicked Submit button.")
    def click_save(self):
        self.logger.debug("Clicking Submit button.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.save_button_xpath))
        ).click()
        self.logger.debug("Clicked Submit button.")

    def click_edit_module(self):
        self.logger.debug("Clicking Edit Module icon.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.edit_icon_xpath))
        ).click()
        self.logger.debug("Clicked Edit Module icon.")

    def click_disable_button(self):
        self.logger.debug("Clicking Disable button.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.disable_button_xpath))
        ).click()
        self.logger.debug("Clicked Disable button.")

    def add_question(self, level_xpath: str, question_text: str):
        self.logger.debug("Adding question to level with xpath: %s", level_xpath)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.maker_module_button_xpath))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, level_xpath))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_questions_button_xpath))).click()
        sleep(1)

        self.logger.debug("Entering question text.")
        input_field = self.wait.until(EC.presence_of_element_located((By.XPATH, self.input_frame_xpath)))
        input_field.click()
        input_field.send_keys(question_text)
        self.logger.debug("Entered question text.")

        self.logger.debug("Submitting question.")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.submit_button_xpath))).click()
        sleep(1)
        self.logger.debug("Submitted question.")

    def add_level1_question(self, question: str):
        self.logger.debug("Adding level 1 question.")
        self.add_question(self.level1_questions_add_xpath, question)
        self.logger.debug("Added level 1 question.")

    def add_level2_question(self, question: str):
        self.logger.debug("Adding level 2 question.")
        self.add_question(self.level2_questions_add_xpath, question)
        self.logger.debug("Added level 2 question.")

    def add_level3_question(self, question: str):
        self.logger.debug("Adding level 3 question.")
        self.add_question(self.level3_questions_add_xpath, question)
        self.logger.debug("Added level 3 question.")