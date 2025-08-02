from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.bridgelabz.utilities.logger import Logger


class COELabs:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = Logger.get_logger(self.__class__.__name__)

    # XPaths and identifiers
    create_COE_button_xpath = "//button[normalize-space()='CREATE COE']"
    COE_textbox_name = "COE"
    COE_details_name = "labDetails"
    latitude_name = "latitude"
    longitude_name = "longitude"
    geo_fencing_distance_name = "distance"
    create_button_xpath = "//button[normalize-space()='Create']"
    edit_button_SRMTN_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[6]/button[1]/*[name()='svg'][1]"
    edit_button_xpath = "//button[normalize-space()='Edit']"
    no_of_learner_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[5]"
    download_sample_csv_xpath = "//button[normalize-space()='Download Sample CSV']"
    download_learner_data_csv_xpath = "(//button[normalize-space()='Download Learner Data'])[1]"
    upload_csv_btn_xpath = "(//label[normalize-space()='Upload CSV'])[1]"
    group_dropdown_xpath = "/html[1]/body[1]/div[4]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]"
    file_input_xpath = "//input[@type='file' and @accept='.csv']"
    submit_csv_btn_xpath = "(//button[normalize-space()='Submit'])[1]"
    coe_next_page_button_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/button[2]"
    coe_disable_button_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[6]/button[2]"
    #the above xpath is for the disable button of the 'sample COE' COE

    def click_create_coe_button(self):
        self.logger.info("Clicking CREATE COE button.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.create_COE_button_xpath))).click()
        self.logger.info("CREATE COE button clicked successfully.")

    def fill_create_coe_form(self, coe_name, details, latitude, longitude, distance):
        self.logger.info(f"Filling COE form with: {coe_name}, {details}, {latitude}, {longitude}, {distance}")
        self.driver.find_element(By.NAME, self.COE_textbox_name).send_keys(coe_name)
        self.driver.find_element(By.NAME, self.COE_details_name).send_keys(details)
        self.driver.find_element(By.NAME, self.latitude_name).send_keys(latitude)
        self.driver.find_element(By.NAME, self.longitude_name).send_keys(longitude)
        self.driver.find_element(By.NAME, self.geo_fencing_distance_name).send_keys(distance)
        self.logger.info("COE form filled successfully.")

    def click_create_button(self):
        self.logger.info("Clicking Create button.")
        self.driver.find_element(By.XPATH, self.create_button_xpath).click()
        self.logger.info("Create button clicked.")

    def click_edit_SRMTN_button(self):
        self.logger.info("Clicking edit button for SRMTN.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.edit_button_SRMTN_xpath))).click()
        self.logger.info("Edit button clicked for SRMTN.")

    def edit_details(self, new_details):
        self.logger.info(f"Editing COE details to: {new_details}")
        details_box = self.driver.find_element(By.NAME, self.COE_details_name)
        actions = ActionChains(self.driver)
        actions.click(details_box)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        details_box.send_keys(new_details)
        self.logger.info("COE details edited successfully.")

    def click_edit_button(self):
        self.logger.info("Clicking Edit button.")
        edit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.edit_button_xpath)))
        edit_button.click()
        self.logger.info("Edit button clicked.")

    def click_disable_button(self):
        self.logger.info("Clicking Next button.")
        next_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.coe_next_page_button_xpath)))
        next_button.click()
        self.logger.info("Clicking Disable button.")
        disable_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.coe_disable_button_xpath)))
        disable_button.click()
        self.logger.info("Disable button clicked.")

    def click_learner_button(self):
        self.logger.info("Clicking Learner count button.")
        learner_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.no_of_learner_xpath)))
        learner_button.click()
        self.logger.info("Learner button clicked.")

    def click_download_sample_csv(self):
        self.logger.info("Clicking Download Sample CSV button.")
        download_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.download_sample_csv_xpath)))
        download_button.click()
        self.logger.info("Sample CSV downloaded.")

    def click_download_learner_data_csv(self):
        self.logger.info("Clicking Download Learner Data CSV button.")
        download_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.download_learner_data_csv_xpath)))
        download_button.click()
        self.logger.info("Learner Data CSV downloaded.")

    def upload_csv_file(self, file_path: str):
        self.logger.info(f"Uploading CSV file from path: {file_path}")

        upload_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.upload_csv_btn_xpath)))
        upload_btn.click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.group_dropdown_xpath))
        ).send_keys("TestQA")
        sleep(1)
        ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

        file_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.file_input_xpath)))
        file_input.send_keys(file_path)
        self.logger.info("CSV file path entered.")

        sleep(5)
        submit_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.submit_csv_btn_xpath)))
        submit_btn.click()
        self.logger.info("CSV file submitted successfully.")
