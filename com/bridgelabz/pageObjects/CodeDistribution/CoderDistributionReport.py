from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from com.bridgelabz.utilities.logger import Logger  # Logging utility

class CoderDistributionReport:
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger.get_logger(self.__class__.__name__)

        # XPaths for dropdowns and button
        self.tab_xpath = "//span[normalize-space()='Coder Distribution']"
        self.coe_dropdown_xpath = "(//div[@id='coe-select'])[1]"
        self.lab_type_dropdown_xpath = "(//div[@id='coe-select'])[2]"
        self.view_button_xpath = "//button[normalize-space()='VIEW']"

    def select_combobox_option(self, dropdown_xpath, value):
        self.logger.info(f"Selecting value '{value}' from dropdown: {dropdown_xpath}")
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
        )
        dropdown.click()
        sleep(0.5)
        option_xpath = f"//li[normalize-space()='{value}']"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()
        self.logger.info(f"Selected option '{value}'")

    def view_coder_distribution_report(self, coe, lab_type):
        self.logger.info("Opening Coder Distribution Report tab")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.tab_xpath))
        ).click()
        self.logger.info("Coder Distribution tab clicked")

        # Select COE and Lab Type
        self.select_combobox_option(self.coe_dropdown_xpath, coe)
        self.select_combobox_option(self.lab_type_dropdown_xpath, lab_type)

        # Click on View button
        self.logger.info("Clicking on VIEW button")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.view_button_xpath))
        ).click()
        sleep(1)

        # Validation
        if "#Fast Coder" in self.driver.page_source:
            self.logger.info("Coder Distribution Report loaded successfully with valid data")
        else:
            self.logger.error("Coder Distribution Report data not found!")
            raise AssertionError("Coder Distribution Report data not found.")
