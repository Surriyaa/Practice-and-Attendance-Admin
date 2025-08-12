"""from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from com.bridgelabz.testcases.conftest import take_screenshot
from com.bridgelabz.utilities.logger import Logger

class PHPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger.get_logger(self.__class__.__name__)

    ph_tab_xpath = "//span[normalize-space()='Practice Head']"
    add_ph_button_xpath = "(//button[normalize-space()='CREATE Practice Head'])[1]"
    name_input_xpath = "//input[@name='name']"
    email_input_xpath = "//input[@name='email']"
    contact_input_xpath = "//input[@name='mobile']"
    base_coe_dropdown_xpath = "//div[@id='mui-component-select-basecoe']"
    create_button_xpath = "(//button[normalize-space()='Create'])[1]"
    edit_icon_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[5]/button[1]"
    update_button_xpath = "(//button[normalize-space()='Update'])[1]"
    disable_button_xpath="/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[6]/td[5]/button[2]"


    def click_ph_tab(self):
        self.logger.info("Initializing WebDriverWait with 20 seconds")
        wait = WebDriverWait(self.driver, 20)
        self.logger.info("Waiting for Practice Head tab to be clickable")
        ph_tab = wait.until(EC.element_to_be_clickable((By.XPATH, self.ph_tab_xpath)))
        self.logger.info("Clicking Practice Head tab")
        ph_tab.click()

    def click_add_ph_button(self):
        self.logger.info("Initializing WebDriverWait with 20 seconds")
        wait = WebDriverWait(self.driver, 20)
        self.logger.info("Waiting for 'CREATE Practice Head' button to be clickable")
        add_ph_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.add_ph_button_xpath)))
        self.logger.info("Clicking 'CREATE Practice Head' button")
        add_ph_button.click()

    def enter_name(self, name):
        self.logger.info(f"Entering name: {name}")
        self.driver.find_element(By.XPATH, self.name_input_xpath).send_keys(name)

    def enter_email(self, email):
        self.logger.info(f"Entering email: {email}")
        self.driver.find_element(By.XPATH, self.email_input_xpath).send_keys(email)

    def enter_mobile(self, mobile):
        self.logger.info(f"Entering mobile: {mobile}")
        self.driver.find_element(By.XPATH, self.contact_input_xpath).send_keys(mobile)

    def select_base_coe(self, base_coe_name):
        self.logger.info("Opening base COE dropdown")
        self.driver.find_element(By.XPATH, self.base_coe_dropdown_xpath).click()

        option_xpath = f"//li[normalize-space()='{base_coe_name}']"
        self.logger.info(f"Waiting for base COE option '{base_coe_name}' to be clickable")
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
            self.logger.info(f"Clicking base COE option '{base_coe_name}'")
            self.driver.find_element(By.XPATH, option_xpath).click()
        except Exception as e:
            self.logger.error(f"Error occurred while selecting base COE: {e}")
        self.logger.info("Sleeping for 2 seconds after COE selection")
        sleep(2)

    def click_create_button(self):
        self.logger.info("Clicking Create button")
        self.driver.find_element(By.XPATH, self.create_button_xpath).click()
        self.logger.info("Sleeping for 4 seconds after Create")
        sleep(1)

    def verify_email(self, email):
        self.logger.info(f"Verifying if email '{email}' is present in page source")
        assert email in self.driver.page_source, f"Email '{email}' not found on the page!"
        self.logger.info(f"Practice Head Email '{email}' is present on the page, So PH is Created Successfully")
        print(f"Practice Head Email '{email}' is present on the page, So PH is Created Successfully")

    def click_edit_icon(self):
        self.logger.info("Initializing WebDriverWait with 20 seconds")
        wait = WebDriverWait(self.driver, 20)
        self.logger.info("Waiting for Edit icon to be clickable")
        edit_icon = wait.until(EC.element_to_be_clickable((By.XPATH, self.edit_icon_xpath)))
        self.logger.info("Clicking Edit icon")
        edit_icon.click()

    def enter_new_mobile(self, mobile):
        self.logger.info("Locating contact input field")
        contact_field = self.driver.find_element(By.XPATH, self.contact_input_xpath)
        self.logger.info("Focusing contact input field")
        contact_field.click()
        self.logger.info("Clearing contact input field using CTRL+A and DELETE")
        contact_field.send_keys(Keys.CONTROL + "a")
        contact_field.send_keys(Keys.DELETE)
        self.logger.info(f"Entering new mobile: {mobile}")
        contact_field.send_keys(mobile)
        self.logger.info("Sleeping for 3 seconds after entering mobile")
        sleep(1)

    def click_update_button(self):
        self.logger.info("Clicking Update button")
        self.driver.find_element(By.XPATH, self.update_button_xpath).click()
        self.logger.info("Sleeping for 3 seconds after Update")
        sleep(3)

    def click_disable_button(self):
        self.logger.info("Initializing WebDriverWait with 20 seconds")
        wait = WebDriverWait(self.driver, 20)
        self.logger.info("Waiting for Disable button to be clickable")
        self.driver.find_element(By.XPATH, self.disable_button_xpath).click()
        # Verify success toast
        toast_xpath = "//*[contains(text(),'disabled successfully')]"
        try:
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            print("Toast message verified: File upload successfully.")
        except Exception as e:
            take_screenshot(self.driver, "upload_csv_file")
            raise AssertionError("Toast message not found or mismatch. " + str(e))"""