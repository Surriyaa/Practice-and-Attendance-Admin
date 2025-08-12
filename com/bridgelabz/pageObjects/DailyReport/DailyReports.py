from datetime import datetime
from time import sleep
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.bridgelabz.utilities.logger import Logger


class DailyReports:
    def __init__(self, driver, tc_id=None):
        self.driver = driver
        self.logger = Logger.get_logger(self.__class__.__name__, tc_id)

    daily_reports_tab_xpath = "//span[normalize-space()='Daily Report']"

    # XPaths for Daily Attendance Report
    view_daily_attendance_tab_xpath = "(//button[normalize-space()='VIEW DAILY ATTENDANCE REPORT'])[1]"
    coe_dropdown_xpath = "(//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-formControl MuiInputBase-sizeSmall MuiSelect-root css-iz33ar'])[1]"
    lab_type_dropdown_xpath = "//label[text()='Lab Type*']/following-sibling::div//div[@role='combobox']"
    attendance_name_dropdown_xpath = "//label[normalize-space()='Attendance Name*']/following-sibling::div//input"
    session_time_dropdown_xpath = "//label[normalize-space()='Session Time']/following-sibling::div//div[@role='combobox']"
    from_date_xpath = "//input[@name='fromDate']"
    to_date_xpath = "//input[@name='toDate']"
    view_button_xpath = "(//button[normalize-space()='VIEW'])[1]"

    # XPaths for Daily Practice Report
    view_daily_practice_tab_xpath = "(//button[normalize-space()='VIEW DAILY PRACTICE REPORT'])[1]"
    dp_coe_dropdown_xpath = "//div[@id='mui-component-select-coe']"
    dp_lab_type_dropdown_xpath = "//div[@id='mui-component-select-labType']"
    dp_maker_plan_dropdown_xpath = "//div[@id='mui-component-select-makerPlan']"
    dp_maker_module_dropdown_xpath = "//div[@id='mui-component-select-makerModule']"
    dp_lab_dropdown_xpath = "(//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-formControl MuiInputBase-sizeSmall MuiInputBase-adornedEnd MuiAutocomplete-inputRoot css-1kmkvia'])[1]"
    view_practice_button_xpath = "//button[normalize-space()='VIEW']"

    def select_combobox_option(self, combobox_xpath, option_text):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, combobox_xpath))
        ).click()
        self.logger.info(f"Clicked combobox: {combobox_xpath}")
        sleep(0.5)
        option_xpath = f"//li[normalize-space()='{option_text}']"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()
        self.logger.info(f"Selected option: {option_text}")

    def select_combobox_by_tab(self, combobox_xpath, option_text):
        coe = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, combobox_xpath))
        )
        coe.send_keys(Keys.TAB + Keys.ENTER)
        option_xpath = f"//li[normalize-space()='{option_text}']"
        sleep(0.5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()
        self.logger.info(f"Selected (TAB method) option: {option_text}")

    def set_date_js(self, xpath, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", element, value)
        self.driver.execute_script("""
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, element)
        self.logger.info(f"Date set for {xpath}: {value}")

    def view_daily_attendance_report(self, coe, lab_type, attendance, session, from_date, to_date):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.daily_reports_tab_xpath))
        ).click()
        self.logger.info("Clicked on Daily Report tab")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.view_daily_attendance_tab_xpath))
        ).click()
        self.logger.info("Clicked on View Daily Attendance Report button")

        self.select_combobox_option(self.coe_dropdown_xpath, coe)
        self.select_combobox_option(self.lab_type_dropdown_xpath, lab_type)

        input_xpath = self.attendance_name_dropdown_xpath
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, input_xpath))).send_keys(
            "Day Order1")
        sleep(1)
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.logger.info("Selected attendance name: Day Order1")

        sleep(1)
        self.select_combobox_option(self.session_time_dropdown_xpath, session)

        self.set_date_js(self.from_date_xpath, from_date)
        self.set_date_js(self.to_date_xpath, to_date)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.view_button_xpath))
        ).click()
        self.logger.info("Clicked on View button for Attendance Report")
        sleep(1)

        assert "Total Strength" in self.driver.page_source, "Total Strength column is missing in Daily Attendance Report"
        self.logger.info("Total Strength column is present in Daily Attendance Report — Validation Passed")

    def view_daily_practice_report(self, coe, lab_type, maker_plan, maker_module, lab):
        wait = WebDriverWait(self.driver, 10)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.daily_reports_tab_xpath))
        ).click()
        self.logger.info("Clicked on Daily Report tab")

        practice_tab = wait.until(EC.element_to_be_clickable((By.XPATH, self.view_daily_practice_tab_xpath)))
        practice_tab.click()
        self.logger.info("Clicked on Daily Practice Report tab")

        self.select_combobox_option(self.dp_coe_dropdown_xpath, coe)
        sleep(1)
        self.select_combobox_option(self.dp_lab_type_dropdown_xpath, lab_type)
        self.select_combobox_option(self.dp_maker_plan_dropdown_xpath, maker_plan)
        self.select_combobox_option(self.dp_maker_module_dropdown_xpath, maker_module)
        self.select_combobox_option(self.dp_lab_dropdown_xpath, lab)

        view_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.view_practice_button_xpath)))
        self.driver.execute_script("arguments[0].click();", view_button)
        self.logger.info("Clicked on View button for Daily Practice Report")
        sleep(1)

        if "Lab Strength" in self.driver.page_source:
            self.logger.info("Lab Strength column is present in Daily Practice Report — Validation Passed")
        else:
            self.logger.warning("Lab Strength column is missing in Daily Practice Report")