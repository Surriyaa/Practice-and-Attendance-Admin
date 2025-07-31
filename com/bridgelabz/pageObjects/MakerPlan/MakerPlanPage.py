from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from com.bridgelabz.utilities.logger import Logger  # Adjust the import as needed

class MakerPlanPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger.get_logger(self.__class__.__name__)

    maker_plan_tab_xpath = "//span[normalize-space()='Maker Plan']"
    add_maker_plan_button_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/button[1]/*[name()='svg'][1]"
    name_input_xpath = "//input[@name='makerPlan']"
    duration_input_xpath = "//input[@name='codingHours']"
    description_input_xpath= "//textarea[@name='description']"
    save_button_xpath = "(//button[normalize-space()='Submit'])[1]"
    edit_icon_xpath = "//*[name()='path' and contains(@d,'M3 17.25V2')]"
    duration_edit_xpath = "//input[@name='codingHours']"

    maker_plan_dropdown_xpath = "(//div[@id='maker-plan-select'])"

    def create_maker_plan(self, name, duration, description):
        self.logger.info("Attempting to click on Maker Plan tab.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.maker_plan_tab_xpath))).click()
        
        self.logger.info("Clicking the Add Maker Plan button.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.add_maker_plan_button_xpath))).click()

        self.logger.info(f"Entering Maker Plan name: {name}.")
        self.driver.find_element(By.XPATH, self.name_input_xpath).send_keys(name)
        
        self.logger.info(f"Entering duration: {duration}.")
        self.driver.find_element(By.XPATH, self.duration_input_xpath).send_keys(duration)
        
        self.logger.info(f"Entering description: {description}.")
        self.driver.find_element(By.XPATH, self.description_input_xpath).send_keys(description)
        
        sleep(3)
        self.logger.info("Clicking the Submit button to save the Maker Plan.")
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def edit_module_in_plan(self, maker_plan_name, new_duration):
        wait = WebDriverWait(self.driver, 20)

        self.logger.info("Clicking on the Maker Plan tab.")
        wait.until(EC.element_to_be_clickable((By.XPATH, self.maker_plan_tab_xpath))).click()
        
        sleep(2)
        self.logger.info("Opening the Maker Plan dropdown.")
        wait.until(EC.element_to_be_clickable((By.XPATH, self.maker_plan_dropdown_xpath))).send_keys(Keys.ENTER)
        
        sleep(2)
        self.logger.info(f"Selecting Maker Plan: {maker_plan_name}.")
        option_xpath = f"//li[normalize-space()='{maker_plan_name}']"
        wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath))).click()

        self.logger.info("Clicking the Edit icon for the module.")
        wait.until(EC.element_to_be_clickable((By.XPATH, self.edit_icon_xpath))).click()

        self.logger.info("Locating the duration field to edit.")
        duration_field = wait.until(EC.presence_of_element_located((By.XPATH, self.duration_edit_xpath)))
        
        sleep(2)
        self.logger.info("Clearing the current duration value.")
        duration_field.clear()
        
        sleep(2)
        self.logger.info(f"Entering the new duration: {new_duration}.")
        duration_field.send_keys(new_duration)

        self.logger.info("Clicking the Submit button to save changes.")
        wait.until(EC.element_to_be_clickable((By.XPATH, self.save_button_xpath))).click()