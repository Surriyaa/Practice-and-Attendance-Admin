from time import sleep
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from com.bridgelabz.utilities.logger import Logger

class CheckInOutReport:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = Logger.get_logger(self.__class__.__name__)

        # XPaths
        self.checkinout_tab_xpath = "//span[normalize-space()='CheckIn-Out Report']"
        self.coe_dropdown_xpath = "//label[text()='COE*']/following-sibling::div//div[@role='combobox']"
        self.lab_type_dropdown_xpath = "//label[text()='Lab Type*']/following-sibling::div//div[@role='combobox']"
        self.attendance_name_xpath = "//label[normalize-space()='Attendance Name*']/following-sibling::div//input"
        self.session_time_xpath = "//label[normalize-space()='Session Time']/following-sibling::div//div[@role='combobox']"
        self.from_date_xpath = "//input[@name='fromDate']"
        self.to_date_xpath = "//input[@name='toDate']"
        self.view_button_xpath = "//button[normalize-space()='VIEW']"

    def select_combobox_option(self, combobox_xpath, option_text):
        self.logger.info(f"Selecting option '{option_text}' for dropdown with xpath: {combobox_xpath}")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, combobox_xpath))).click()
        sleep(1)
        option_xpath = f"//li[normalize-space()='{option_text}']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath))).click()
        self.logger.info(f"Option '{option_text}' selected successfully.")

    def set_date_js(self, xpath, value):
        self.logger.info(f"Setting date '{value}' using JS for xpath: {xpath}")
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        self.driver.execute_script("arguments[0].value = arguments[1];", element, value)
        sleep(1)
        self.driver.execute_script("""
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, element)
        self.logger.info(f"Date '{value}' set successfully for xpath: {xpath}")

    def view_checkin_checkout_report(self, coe, lab_type, attendance_name, session_time, from_date, to_date):
        self.logger.info("Navigating to CheckIn-Out Report tab.")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.checkinout_tab_xpath))).click()

        self.logger.info("Filling dropdowns and fields for report generation.")
        self.select_combobox_option(self.coe_dropdown_xpath, coe)
        self.select_combobox_option(self.lab_type_dropdown_xpath, lab_type)

        self.logger.info(f"Typing attendance name: {attendance_name}")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.attendance_name_xpath))).send_keys(attendance_name)
        sleep(1)
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.logger.info("Attendance name selected.")

        self.select_combobox_option(self.session_time_xpath, session_time)

        sleep(2)
        self.set_date_js(self.from_date_xpath, from_date)
        sleep(2)
        self.set_date_js(self.to_date_xpath, to_date)

        self.logger.info("Clicking the VIEW button.")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.view_button_xpath))).click()

        sleep(2)
        if "#CheckIn Count" in self.driver.page_source:
            self.logger.info("CheckIn and CheckOut report validated successfully. '#CheckIn Count' column found.")
        else:
            self.logger.error("CheckIn and CheckOut report validation failed. '#CheckIn Count' column not found.")
            raise AssertionError("#CheckIn Count column is missing in report.")
