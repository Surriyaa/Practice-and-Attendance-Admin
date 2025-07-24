from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LabReports:
    lab_report_tab_xpath="//span[normalize-space()='Lab Report']"
    def __init__(self, driver):
        self.driver = driver

    def select_combobox_option(self, combobox_xpath, option_text):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, combobox_xpath))
        ).click()
        option_xpath = f"//li[normalize-space()='{option_text}']"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()

    def view_lab_report(self):
        wait = WebDriverWait(self.driver, 20)

        # Click on Lab Report tab
        lab_report_tab = wait.until(EC.element_to_be_clickable((By.XPATH, self.lab_report_tab_xpath)))
        lab_report_tab.click()

        # Select COE
        coe_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "mui-component-select-coe")))
        coe_dropdown.click()
        coe_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'P&A Phase 2')]")))
        coe_option.click()

        # Select Lab
        lab_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-sizeSmall MuiInputBase-adornedEnd MuiAutocomplete-inputRoot css-1kmkvia']")))
        lab_dropdown.click()
        lab_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Lab 1')]")))
        lab_option.click()

        # Select Maker Plan
        maker_plan_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "mui-component-select-makerPlan")))
        maker_plan_dropdown.click()
        maker_plan_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'QA')]")))
        maker_plan_option.click()

        # Click View
        view_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'VIEW')]")))
        view_button.click()
        sleep(3)

        # Validate 'Lab Strength' present in page source
        assert "Lab Strength" in self.driver.page_source,"No Data Shown "
        print("Data for the provided Coe is fetched")
