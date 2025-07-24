from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MentorPage:

    def __init__(self, driver):
        self.driver = driver

    mentor_tab_xpath = "//span[normalize-space()='Practice Mentor']"
    add_mentor_button_xpath = "//button[normalize-space()='CREATE Practice Mentor']"
    name_input_xpath = "//input[@name='name']"
    email_input_xpath = "//input[@name='email']"
    contact_input_xpath = "//input[@name='mobile']"
    base_coe_dropdown_xpath = "//div[@id='mui-component-select-basecoe']"
    create_button_xpath = "(//button[normalize-space()='Create'])[1]"
    edit_icon_xpath = "(//*[name()='svg'][@class='MuiSvgIcon-root MuiSvgIcon-fontSizeSmall css-vh810p'])[3]"
    update_button_xpath = "(//button[normalize-space()='Update'])[1]"
    rignt_aro_xpath="/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/button[2]"


    def create_practice_mentor(self, name, email, mobile, base_coe_name):
        wait = WebDriverWait(self.driver, 20)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.mentor_tab_xpath))).click()
        self.driver.find_element(By.XPATH, self.add_mentor_button_xpath).click()
        self.driver.find_element(By.XPATH, self.name_input_xpath).send_keys(name)
        self.driver.find_element(By.XPATH, self.email_input_xpath).send_keys(email)
        self.driver.find_element(By.XPATH, self.contact_input_xpath).send_keys(mobile)
        self.driver.find_element(By.XPATH, self.base_coe_dropdown_xpath).send_keys(Keys.ENTER)

        option_xpath = f"//li[normalize-space()='{base_coe_name}']"
        wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath))).click()
        sleep(2)
        self.driver.find_element(By.XPATH, self.create_button_xpath).click()
        sleep(4)
        arrow=self.driver.find_element(By.XPATH, self.rignt_aro_xpath)
        arrow.click()
        arrow.click()
        arrow.click()
        arrow.click()

        sleep(5)

        assert email in self.driver.page_source, f"Email '{email}' not found on the page!"
        print(f"Practice Mentor Email '{email}' is present on the page, So Mentor is Created Successfully")

    def edit_mentor_contact(self, mobile):
        wait = WebDriverWait(self.driver, 20)

        ph_tab = wait.until(EC.element_to_be_clickable((By.XPATH, self.mentor_tab_xpath)))
        ph_tab.click()

        sleep(2)
        ActionChains(self.driver).send_keys(Keys.TAB * 6).send_keys(Keys.ENTER).perform()

        sleep(3)

        contact_field = self.driver.find_element(By.XPATH, self.contact_input_xpath)

        # Use CTRL+A and DELETE instead of clear()
        contact_field.click()  # Focus the input field
        contact_field.send_keys(Keys.CONTROL + "a")
        contact_field.send_keys(Keys.DELETE)

        contact_field.send_keys(mobile)
        sleep(3)
        self.driver.find_element(By.XPATH, self.update_button_xpath).click()
        sleep(3)
        assert mobile in self.driver.page_source, f"Email '{mobile}' not found on the page!"
        print(f"Practice Mentor Mobile '{mobile}' is present on the page, So Mentor is Updated Successfully")
