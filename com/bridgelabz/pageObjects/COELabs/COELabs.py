from time import sleep

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class COELabs:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    create_COE_button_xpath = "//button[normalize-space()='CREATE COE']"
    COE_textbox_name = "COE"
    COE_details_name = "labDetails"
    latitude_name = "latitude"
    longitude_name = "longitude"
    geo_fencing_distance_name = "distance"
    create_button_xpath = "//button[normalize-space()='Create']"
    edit_button_SRMTN_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[6]/button[1]/*[name()='svg'][1]"
    edit_button_xpath = "//button[normalize-space()='Edit']"
    no_of_learner_xpath="/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[5]"
    download_sample_csv_xpath="//button[normalize-space()='Download Sample CSV']"
    download_learner_data_csv_xpath="(//button[normalize-space()='Download Learner Data'])[1]"
    upload_csv_btn_xpath = "(//label[normalize-space()='Upload CSV'])[1]"
    group_dropdown_xpath = "/html[1]/body[1]/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]"
    file_input_xpath = "//input[@type='file' and @accept='.csv']"
    submit_csv_btn_xpath = "(//button[normalize-space()='Submit'])[1]"

    def click_create_coe_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.create_COE_button_xpath))).click()

    def fill_create_coe_form(self, coe_name, details, latitude, longitude, distance):
        self.driver.find_element(By.NAME, self.COE_textbox_name).send_keys(coe_name)
        self.driver.find_element(By.NAME, self.COE_details_name).send_keys(details)
        self.driver.find_element(By.NAME, self.latitude_name).send_keys(latitude)
        self.driver.find_element(By.NAME, self.longitude_name).send_keys(longitude)
        self.driver.find_element(By.NAME, self.geo_fencing_distance_name).send_keys(distance)

    def click_create_button(self):
        self.driver.find_element(By.XPATH, self.create_button_xpath).click()

    def click_edit_SRMTN_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.edit_button_SRMTN_xpath))).click()

    def edit_details(self, new_details):
        details_box = self.driver.find_element(By.NAME, self.COE_details_name)
        details_box.clear()
        details_box.send_keys(new_details)

    def click_edit_button(self):
        """Wait for the Edit button and click."""
        edit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.edit_button_xpath)))
        edit_button.click()

    def click_learner_button(self):
        """Wait for the Learner button and click."""
        learner_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.no_of_learner_xpath)))
        learner_button.click()

    def click_download_sample_csv(self):
        """Wait for the Download Sample CSV button and click."""
        download_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.download_sample_csv_xpath)))
        download_button.click()

    def click_download_learner_data_csv(self):
        """Wait for the Download Sample CSV button and click."""
        download_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.download_learner_data_csv_xpath)))
        download_button.click()

    def upload_csv_file(self,file_path: str):
        """Select group from dropdown and upload the CSV file."""

        # Wait for and click 'Upload CSV' button
        upload_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.upload_csv_btn_xpath)))
        upload_btn.click()

        # Select group name from dropdown

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.group_dropdown_xpath))).send_keys(
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




