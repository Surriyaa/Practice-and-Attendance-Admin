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
    download_sample_csv_xpath="//label[normalize-space()='Download Sample CSV']"


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


