from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
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
    edit_icon_xpath = "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeSmall css-vh810p'])[3]"
    update_button_xpath = "(//button[normalize-space()='Update'])[1]"

    def create_ph(self, name, email, mobile, base_coe_name):
        self.logger.info("Initializing WebDriverWait with 20 seconds")
        wait = WebDriverWait(self.driver, 20)
        self.logger.info("Waiting for Practice Head tab to be clickable")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ph_tab_xpath)))
        self.logger.info("Clicking Practice Head tab")
        self.driver.find_element(By.XPATH, self.ph_tab_xpath).click()
        self.logger.info("Clicking 'CREATE Practice Head' button")
        self.driver.find_element(By.XPATH, self.add_ph_button_xpath).click()
        self.logger.info(f"Entering name: {name}")
        self.driver.find_element(By.XPATH, self.name_input_xpath).send_keys(name)
        self.logger.info(f"Entering email: {email}")
        self.driver.find_element(By.XPATH, self.email_input_xpath).send_keys(email)
        self.logger.info(f"Entering mobile: {mobile}")
        self.driver.find_element(By.XPATH, self.contact_input_xpath).send_keys(mobile)
        self.logger.info("Opening base COE dropdown")
        self.driver.find_element(By.XPATH, self.base_coe_dropdown_xpath).send_keys(Keys.ENTER)

        option_xpath = f"//li[normalize-space()='{base_coe_name}']"
        self.logger.info(f"Waiting for base COE option '{base_coe_name}' to be clickable")
        wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        self.logger.info(f"Clicking base COE option '{base_coe_name}'")
        self.driver.find_element(By.XPATH, option_xpath).click()
        self.logger.info("Sleeping for 2 seconds after COE selection")
        sleep(2)
        self.logger.info("Clicking Create button")
        self.driver.find_element(By.XPATH, self.create_button_xpath).click()
        self.logger.info("Sleeping for 4 seconds after Create")
        sleep(4)

        self.logger.info(f"Verifying if email '{email}' is present in page source")
        assert email in self.driver.page_source, f"Email '{email}' not found on the page!"
        self.logger.info(f"Practice Head Email '{email}' is present on the page, So PH is Created Successfully")
        print(f"Practice Head Email '{email}' is present on the page, So PH is Created Successfully")

    def edit_ph_contact(self, mobile):
        self.logger.info("Initializing WebDriverWait with 20 seconds")
        wait = WebDriverWait(self.driver, 20)

        self.logger.info("Waiting for Practice Head tab to be clickable")
        ph_tab = wait.until(EC.element_to_be_clickable((By.XPATH, self.ph_tab_xpath)))
        self.logger.info("Clicking Practice Head tab")
        ph_tab.click()

        self.logger.info("Sleeping for 2 seconds before focusing the edit row")
        sleep(2)
        self.logger.info("Sending TAB 7 times and ENTER to focus the edit icon")
        ActionChains(self.driver).send_keys(Keys.TAB * 7).send_keys(Keys.ENTER).perform()

        self.logger.info("Sleeping for 3 seconds after edit icon click")
        sleep(3)

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
        sleep(3)
        self.logger.info("Clicking Update button")
        self.driver.find_element(By.XPATH, self.update_button_xpath).click()
        self.logger.info("Sleeping for 3 seconds after Update")
        sleep(3)