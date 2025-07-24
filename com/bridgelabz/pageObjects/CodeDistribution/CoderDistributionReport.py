from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class CoderDistributionReport:
    def __init__(self, driver):
        self.driver = driver
        # XPaths for dropdowns and button
        self.tab_xpath = "//span[normalize-space()='Coder Distribution']"
        self.coe_dropdown_xpath = "(//div[@id='coe-select'])[1]"
        self.lab_type_dropdown_xpath = "(//div[@id='coe-select'])[2]"
        self.view_button_xpath = "//button[normalize-space()='VIEW']"

    def select_combobox_option(self, dropdown_xpath, value):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
        )
        dropdown.click()
        sleep(1)
        option_xpath = f"//li[normalize-space()='{value}']"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()

    def view_coder_distribution_report(self, coe, lab_type):
        # Click on the left nav tab
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.tab_xpath))
        ).click()

        # Select COE and Lab Type
        self.select_combobox_option(self.coe_dropdown_xpath, coe)
        self.select_combobox_option(self.lab_type_dropdown_xpath, lab_type)

        # Click on View button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.view_button_xpath))
        ).click()

        sleep(2)

        # Validation - check for table column header
        assert "#Fast Coder" in self.driver.page_source,"Coder Distribution Report data not found."
        print("Coder Distribution Report loaded successfully.")
