from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MakerModule:

    def __init__(self, driver):
        self.driver = driver

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

    edit_icon_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[6]/button[1]/*[name()='svg'][1]"  # Edit first record

    # Actions
    def click_maker_module(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.maker_module_button_xpath))
        ).click()

    def click_create_module(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.create_module_button_xpath))
        ).click()

    def select_module_dropdown(self, value):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.select_module_dropdown_xpath))
        )
        drop = Select(self.driver.find_element(By.XPATH, self.select_module_dropdown_xpath))
        drop.select_by_value(str(value))

    def fill_module_form(self, topic, notes, level1, level2, level3):
        self.driver.find_element(By.XPATH,self.topic_input_xpath).send_keys(topic)
        self.driver.find_element(By.XPATH,self.notes_input_xpath).send_keys(notes)
        self.driver.find_element(By.XPATH,self.level1_input_xpath).send_keys(level1)
        self.driver.find_element(By.XPATH,self.level2_input_xpath).send_keys(level2)
        self.driver.find_element(By.XPATH,self.level3_input_xpath).send_keys(level3)

    def click_submit(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.submit_button_xpath))
        ).click()

    def click_edit_module(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.edit_icon_xpath))
        ).click()
