from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LabPractice:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    lab_practice_tab_xpath="//span[normalize-space()='Lab Practice']"

    create_lab_button_xpath = "(//button[normalize-space()='Create lab'])[1]"
    coe_dropdown_xpath ="/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]"
    coe_select_xpath="//div[@id='mui-component-select-COE']"
    lab_name_xpath ="/html[1]/body[1]/div[3]/div[3]/form[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
    session_start_xpath="/html[1]/body[1]/div[3]/div[3]/form[1]/div[1]/div[3]/div[1]/div[1]/input[1]"
    session_end_xpath="/html[1]/body[1]/div[3]/div[3]/form[1]/div[1]/div[4]/div[1]/div[1]/input[1]"
    main_mentor_dropdown_xpath="//div[@id='mui-component-select-mainMentor']"
    sub_mentor_dropdown_xpath="//div[@id='mui-component-select-supportMentor']"
    lab_type_xpath="(//input[@value='Fellowship'])[1]"
    edit_button_newbuild_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[7]/button[1]"
    edit_button_xpath = "//button[normalize-space()='Edit']"
    click_create_xpath = "(//button[normalize-space()='Create'])[1]"
    update_button_xpath = "(//button[normalize-space()='Update'])[1]"
    download_sample_csv_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]"
    upload_csv_btn_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]"
    download_lab_data_csv_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]"

    def select_combobox_option(self, combobox_xpath, option_text):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, combobox_xpath))
        ).click()
        sleep(2)
        option_xpath = f"//li[normalize-space()='{option_text}']"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()
        sleep(1)

    def select_coe(self,coe):
        # Navigate to tab
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lab_practice_tab_xpath))
        ).click()
        self.select_combobox_option(self.coe_dropdown_xpath,coe)
        sleep(1)
        self.driver.find_element(By.XPATH,"(//button[normalize-space()='View'])[1]").click()

    def click_create_lab_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.create_lab_button_xpath))).click()

    def set_date_js(self, xpath, value):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", element, value)
        # Optional: fire change/input event in case app listens to them
        self.driver.execute_script("""
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, element)
        print(f"Set date {value} for {xpath}")

    def create_lab(self, coe, lab_name, start_time, end_time,main_mentor,support_mentor, lab_type):

        # Dropdowns
        self.select_combobox_option(self.coe_select_xpath, coe)

        # Attendance name
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lab_name_xpath))
        ).send_keys(lab_name)

        '''# Time fields
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.session_start_xpath))
        ).send_keys(start_time)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.session_end_xpath))
        ).send_keys(end_time)'''

        # Time fields
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.session_start_xpath))
        ).send_keys(start_time)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.session_end_xpath))
        ).send_keys(end_time)

        self.select_combobox_option(self.main_mentor_dropdown_xpath, main_mentor)
        self.select_combobox_option(self.sub_mentor_dropdown_xpath, support_mentor)
        self.driver.find_element(By.XPATH, self.lab_type_xpath).click()
        self.driver.find_element(By.XPATH, self.click_create_xpath).click()

        sleep(3)
        assert lab_name in self.driver.page_source, "lab not created or not displayed."
        print("lab created successfully.")

    def click_edit_newbuild_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.edit_button_newbuild_xpath))).click()

    def click_download_sample_lab_csv(self):
            """Wait for the Download Sample CSV button and click."""
            download_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.download_sample_csv_xpath)))
            download_button.click()

    def edit_details(self, new_lab_name):
        details_box = self.driver.find_element(By.XPATH, self.lab_name_xpath)
        details_box.click()
        ActionChains(self.driver) \
            .key_down(Keys.CONTROL) \
            .send_keys("a") \
            .key_up(Keys.CONTROL) \
            .send_keys(Keys.DELETE) \
            .perform()
        sleep(2)
        details_box.send_keys(new_lab_name)
        self.driver.find_element(By.XPATH, self.update_button_xpath).click()
        sleep(3)

        assert new_lab_name in self.driver.page_source, "lab not edited or not displayed."
        print("lab edited successfully.")

    def click_download_lab_data_csv(self):
        """Wait for the Download Sample CSV button and click."""
        download_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.download_lab_data_csv_xpath)))
        download_button.click()

    def upload_lab_csv_file(self, file_path: str):
        """Select group from dropdown and upload the CSV file."""

        # Wait for and click 'Upload CSV' button
        upload_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.upload_csv_btn_xpath)))
        upload_btn.click()

        # Select group name from dropdown

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.group_dropdown_xpath))).send_keys(
            "TestQA")
        sleep(1)
        action = ActionChains(self.driver)
        action.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

        # Upload the CSV file
        file_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.file_input_xpath)))
        file_input.send_keys(file_path)
        sleep(5)

        # Click Submit button
        submit_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.submit_csv_btn_xpath)))
        submit_btn.click()
