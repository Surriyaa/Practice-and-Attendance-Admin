# pages/admin_page.py
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

from com.bridgelabz.utilities.logger import Logger
class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger.get_logger(self.__class__.__name__)

        # XPaths
        self.admin_tab_xpath = "//span[text()='Admin']"
        self.add_admin_button_xpath = "(//button[normalize-space()='ADD ADMIN'])[1]"
        self.role_dropdown_xpath = "//div[@id='mui-component-select-role']"
        self.role_option_xpath = "//li[contains(text(),'Super Admin')]"
        self.email_input_xpath = "/html[1]/body[1]/div[3]/div[3]/form[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
        self.mobile_input_xpath = "//input[@name='mobile']"
        self.create_button_xpath = "(//button[normalize-space()='Create'])[1]"
        self.cancel_button_xpath = "(//button[normalize-space()='Cancel'])[1]"
        self.update_button_xpath = "(//button[normalize-space()='Update'])[1]"
        self.toast_msg_xpath = "//*[contains(text(),'successfully')]"

        self.edit_icon_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[9]/td[5]/button[1]"


    def navigate_to_admin_tab(self):
        self.logger.info("Navigating to Admin tab")
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.admin_tab_xpath))).click()

    def click_add_admin(self):
        self.logger.info("Clicking on Add Admin button")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.add_admin_button_xpath))).click()

    def enter_admin_details(self, role, email, mobile):
        self.logger.info("Entering admin details")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.role_dropdown_xpath))).click()
        self.logger.info("Selecting Super Admin role")
        option_xpath = f"//li[normalize-space()='{role}']"
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath))).click()
        self.logger.info("Clearing and entering email and mobile")
        self.logger.info("Clearing and entering email and mobile")
        action = ActionChains(self.driver)
        action.click(self.driver.find_element(By.XPATH, self.email_input_xpath))
        action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        self.logger.info(f"Entering email")
        self.driver.find_element(By.XPATH, self.email_input_xpath).send_keys(email)
        action.click(self.driver.find_element(By.XPATH, self.mobile_input_xpath))
        action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        self.logger.info(f"Entering mobile")
        self.driver.find_element(By.XPATH, self.mobile_input_xpath).send_keys(mobile)

    def click_create(self):
        self.logger.info("Clicking on Create button")
        self.driver.find_element(By.XPATH, self.create_button_xpath).click()

    def click_cancel(self):
        self.logger.info("Clicking on Cancel button")
        self.driver.find_element(By.XPATH, self.cancel_button_xpath).click()

    def get_toast_message(self):
        try:
            self.logger.info("Getting toast message")
            toast = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, self.toast_msg_xpath)))
            self.logger.info("Toast message found")
            return toast.text
        except TimeoutException:
            return ""

    def click_edit_admin(self):
        self.logger.info("Clicking on Edit Admin button")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.edit_icon_xpath))).click()

    def edit_admin_contact_details(self, mobile):
        self.logger.info("Clearing and entering mobile")
        action = ActionChains(self.driver)
        action.click(self.driver.find_element(By.XPATH, self.mobile_input_xpath))
        action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        self.logger.info(f"Entering mobile")
        self.driver.find_element(By.XPATH, self.mobile_input_xpath).send_keys(mobile)

    def click_update(self):
        self.logger.info("Clicking on Update button")
        self.driver.find_element(By.XPATH, self.update_button_xpath).click()