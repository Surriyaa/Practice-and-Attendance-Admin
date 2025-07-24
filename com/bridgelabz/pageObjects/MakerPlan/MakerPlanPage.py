from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MakerPlanPage:

    def __init__(self, driver):
        self.driver = driver

    maker_plan_tab_xpath = "//span[normalize-space()='Maker Plan']"
    add_maker_plan_button_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/button[1]/*[name()='svg'][1]"
    name_input_xpath = "//input[@name='makerPlan']"
    duration_input_xpath = "//input[@name='codingHours']"
    description_input_xpath= "//textarea[@name='description']"
    save_button_xpath = "//button[normalize-space()='Save']"
    edit_icon_xpath = "//*[name()='path' and contains(@d,'M3 17.25V2')]"
    duration_edit_xpath = "//input[@name='codingHours']"

    maker_plan_dropdown_xpath="(//div[@id='maker-plan-select'])"

    def create_maker_plan(self, name, duration,description):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.maker_plan_tab_xpath))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.add_maker_plan_button_xpath))).click()

        self.driver.find_element(By.XPATH, self.name_input_xpath).send_keys(name)
        self.driver.find_element(By.XPATH, self.duration_input_xpath).send_keys(duration)
        self.driver.find_element(By.XPATH, self.description_input_xpath).send_keys(description)
        sleep(3)
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def edit_module_in_plan(self, maker_plan_name, new_duration):
        wait = WebDriverWait(self.driver, 20)

        # Click Maker Plan tab
        wait.until(EC.element_to_be_clickable((By.XPATH, self.maker_plan_tab_xpath))).click()
        sleep(2)
        # Click Dropdown to open options
        wait.until(EC.element_to_be_clickable((By.XPATH, self.maker_plan_dropdown_xpath))).send_keys(Keys.ENTER)
        sleep(2)

        # Select Maker Plan by name
        option_xpath = f"//li[normalize-space()='{maker_plan_name}']"
        wait.until(EC.element_to_be_clickable((By.XPATH, option_xpath))).click()

        # Click Edit icon of the module
        wait.until(EC.element_to_be_clickable((By.XPATH, self.edit_icon_xpath))).click()

        # Edit duration
        duration_field = wait.until(EC.presence_of_element_located((By.XPATH, self.duration_edit_xpath)))
        sleep(2)
        duration_field.clear()
        sleep(2)
        duration_field.send_keys(new_duration)

        # Submit
        wait.until(EC.element_to_be_clickable((By.XPATH, self.save_button_xpath))).click()

