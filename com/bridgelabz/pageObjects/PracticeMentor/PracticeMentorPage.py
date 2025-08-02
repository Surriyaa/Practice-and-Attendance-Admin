from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from com.bridgelabz.utilities.logger import Logger


class MentorPage:
    mentor_tab_xpath = "//span[normalize-space()='Practice Mentor']"
    add_mentor_button_xpath = "//button[normalize-space()='CREATE Practice Mentor']"
    name_input_xpath = "//input[@name='name']"
    email_input_xpath = "//input[@name='email']"
    contact_input_xpath = "//input[@name='mobile']"
    base_coe_dropdown_xpath = "//div[@id='mui-component-select-basecoe']"
    create_button_xpath = "(//button[normalize-space()='Create'])[1]"
    edit_icon_xpath = "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeSmall css-vh810p'])[3]"
    update_button_xpath = "(//button[normalize-space()='Update'])[1]"
    rignt_aro_xpath = (
        "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/button[2]"
    )
    disable_button_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[7]/td[5]/button[2]"

    def __init__(self, driver):
        self.driver = driver
        self.logger = Logger.get_logger(self.__class__.__name__)

    def create_practice_mentor(self, name, email, mobile, base_coe_name):
        self.logger.info("Initializing wait for mentor creation.")
        wait = WebDriverWait(self.driver, 15)

        self.logger.info("Waiting for mentor tab to be clickable.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.mentor_tab_xpath))
        )

        self.logger.info("Clicking mentor tab.")
        self.driver.find_element(By.XPATH, self.mentor_tab_xpath).click()

        self.logger.info("Clicking add mentor button.")
        self.driver.find_element(By.XPATH, self.add_mentor_button_xpath).click()

        self.logger.info(f"Entering mentor name: {name}")
        self.driver.find_element(By.XPATH, self.name_input_xpath).send_keys(name)

        self.logger.info(f"Entering mentor email: {email}")
        self.driver.find_element(By.XPATH, self.email_input_xpath).send_keys(email)

        self.logger.info(f"Entering mentor mobile: {mobile}")
        self.driver.find_element(By.XPATH, self.contact_input_xpath).send_keys(mobile)

        self.logger.info("Opening base COE dropdown.")
        self.driver.find_element(By.XPATH, self.base_coe_dropdown_xpath).send_keys(Keys.ENTER)

        option_xpath = f"//li[normalize-space()='{base_coe_name}']"
        self.logger.info(f"Waiting for base COE option '{base_coe_name}' to be clickable.")
        wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath)))

        self.logger.info(f"Clicking base COE option: {base_coe_name}")
        self.driver.find_element(By.XPATH, option_xpath).click()

        self.logger.info("Sleeping for 2 seconds after selecting COE.")
        sleep(2)

        self.logger.info("Clicking create button.")
        self.driver.find_element(By.XPATH, self.create_button_xpath).click()
        sleep(1)
        self.logger.info("Locating right arrow for navigation.")
        arrow = self.driver.find_element(By.XPATH, self.rignt_aro_xpath)

        for i in range(4):
            self.logger.info(f"Clicking right arrow (iteration {i+1}).")
            arrow.click()

        self.logger.info("Sleeping for 5 seconds after arrow navigation.")
        sleep(5)

        self.logger.info(f"Asserting that mentor email '{email}' is present on the page.")
        assert email in self.driver.page_source, f"Email '{email}' not found on the page!"

        self.logger.info(
            f"Practice Mentor Email '{email}' is present on the page, So Mentor is Created Successfully"
        )
        print(
            f"Practice Mentor Email '{email}' is present on the page, So Mentor is Created Successfully"
        )

    def edit_mentor_contact(self, mobile):
        self.logger.info("Initializing wait for mentor editing.")
        wait = WebDriverWait(self.driver, 20)

        self.logger.info("Waiting for mentor tab to be clickable.")
        ph_tab = wait.until(EC.element_to_be_clickable((By.XPATH, self.mentor_tab_xpath)))

        self.logger.info("Clicking mentor tab.")
        ph_tab.click()
        sleep(1)
        self.logger.info("Sending TABs and ENTER to reach edit icon.")
        ActionChains(self.driver).send_keys(Keys.TAB * 6).send_keys(Keys.ENTER).perform()
        sleep(1)
        self.logger.info("Locating contact input field for editing.")
        contact_field = self.driver.find_element(By.XPATH, self.contact_input_xpath)

        self.logger.info("Clicking contact input field to focus.")
        contact_field.click()

        self.logger.info("Sending CTRL+A to select all in contact field. and delete it.")
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()

        self.logger.info(f"Sending new mobile: {mobile}")
        contact_field.send_keys(mobile)
        sleep(1)
        self.logger.info("Clicking update button.")
        self.driver.find_element(By.XPATH, self.update_button_xpath).click()
        sleep(1)

        self.logger.info(f"Asserting that new mobile '{mobile}' is present on the page.")
        assert mobile in self.driver.page_source, f"Email '{mobile}' not found on the page!"

        self.logger.info(
            f"Practice Mentor Mobile '{mobile}' is present on the page, So Mentor is Updated Successfully"
        )
        print(
            f"Practice Mentor Mobile '{mobile}' is present on the page, So Mentor is Updated Successfully"
        )

    def disable_mentor(self):
        self.logger.info("Initializing wait for mentor editing.")
        wait = WebDriverWait(self.driver, 10)

        self.logger.info("Waiting for mentor tab to be clickable.")
        wait.until(EC.element_to_be_clickable((By.XPATH, self.mentor_tab_xpath))).click()

        wait.until(EC.element_to_be_clickable((By.XPATH, self.disable_button_xpath))).click()

        try:
            toast_xpath = "//*[contains(text(),'disabled successfully')]"
            wait.until(EC.visibility_of_element_located((By.XPATH, toast_xpath)))
            print("Toast message verified: disabled successfully.")
        except Exception as e:
            raise AssertionError("Toast message not found or mismatch. " + str(e))