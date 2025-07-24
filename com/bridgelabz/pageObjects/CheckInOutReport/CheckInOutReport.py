from time import sleep
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckInOutReport:
    def __init__(self, driver):
        self.driver = driver

    # XPaths
    checkinout_tab_xpath = "//span[normalize-space()='CheckIn-Out Report']"
    coe_dropdown_xpath = "//label[text()='COE*']/following-sibling::div//div[@role='combobox']"
    lab_type_dropdown_xpath = "//label[text()='Lab Type*']/following-sibling::div//div[@role='combobox']"
    attendance_name_xpath = "//label[normalize-space()='Attendance Name*']/following-sibling::div//input"
    session_time_xpath = "//label[normalize-space()='Session Time']/following-sibling::div//div[@role='combobox']"
    from_date_xpath = "//input[@name='fromDate']"
    to_date_xpath = "//input[@name='toDate']"
    view_button_xpath = "//button[normalize-space()='VIEW']"

    def select_combobox_option(self, combobox_xpath, option_text):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, combobox_xpath))
        ).click()
        sleep(1)
        option_xpath = f"//li[normalize-space()='{option_text}']"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()

    def set_date_js(self, xpath, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", element, value)
        sleep(1)
        self.driver.execute_script("""
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, element)
        print(f"Set date {value} for {xpath}")

    def view_checkin_checkout_report(self, coe, lab_type, attendance_name, session_time, from_date, to_date):
        # Click on tab
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.checkinout_tab_xpath))
        ).click()
        print("Clicked CheckIn and CheckOut tab")

        # Dropdown selections
        self.select_combobox_option(self.coe_dropdown_xpath, coe)
        print("Selected COE")
        self.select_combobox_option(self.lab_type_dropdown_xpath, lab_type)
        print("Selected Lab Type")

        # Attendance Name autocomplete
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.attendance_name_xpath))
        ).send_keys(attendance_name)
        sleep(1)
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        print("Selected Attendance Name")

        # Session Time
        self.select_combobox_option(self.session_time_xpath, session_time)
        print("Selected Session Time")
        sleep(2)
        # Set dates
        self.set_date_js(self.from_date_xpath, from_date)
        sleep(2)
        self.set_date_js(self.to_date_xpath, to_date)
        print("Set date range")

        # Click View
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.view_button_xpath))
        ).click()
        print("Clicked VIEW button")

        sleep(2)
        assert "#CheckIn Count" in self.driver.page_source, "#CheckIn Count column is missing in report"
        print("#CheckIn Counte column is present. CheckIn and CheckOut Report is Validated.")
