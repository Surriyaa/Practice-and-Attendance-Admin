from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.bridgelabz.utilities.logger import Logger
class LabPractice:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = Logger.get_logger(self.__class__.__name__)

    lab_practice_tab_xpath = "//span[normalize-space()='Lab Practice']"
    submit_csv_btn_xpath = "(//button[contains(text(),'🚀 Submit')])[1]"
    create_lab_button_xpath = "(//button[normalize-space()='Create lab'])[1]"
    coe_dropdown_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]"
    coe_select_xpath = "//div[@id='mui-component-select-COE']"
    lab_name_xpath = "/html[1]/body[1]/div[3]/div[3]/form[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
    session_start_xpath = "/html[1]/body[1]/div[3]/div[3]/form[1]/div[1]/div[3]/div[1]/div[1]/input[1]"
    session_end_xpath = "/html[1]/body[1]/div[3]/div[3]/form[1]/div[1]/div[4]/div[1]/div[1]/input[1]"
    main_mentor_dropdown_xpath = "//div[@id='mui-component-select-mainMentor']"
    sub_mentor_dropdown_xpath = "//div[@id='mui-component-select-supportMentor']"
    lab_type_xpath = "(//input[@value='Fellowship'])[1]"
    edit_button_newbuild_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[7]/button[1]"
    edit_button_xpath = "//button[normalize-space()='Edit']"
    click_create_xpath = "(//button[normalize-space()='Create'])[1]"
    update_button_xpath = "(//button[normalize-space()='Update'])[1]"
    download_sample_csv_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]"
    upload_csv_btn_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]"
    download_lab_data_csv_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]"
    disable_lab_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/button[2]"
    disable_confirm_xpath = "(//button[normalize-space()='Yes, Disable'])[1]"
    file_input_xpath = "//input[@type='file' and @accept='.csv']"

    def select_combobox_option(self, combobox_xpath, option_text):
        self.logger.debug(f"Selecting option '{option_text}' from combobox.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, combobox_xpath))
        ).click()
        sleep(2)
        option_xpath = f"//li[normalize-space()='{option_text}']"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, option_xpath))
        ).click()
        sleep(1)

    def select_coe(self, coe):
        self.logger.info(f"Selecting COE: {coe}")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lab_practice_tab_xpath))
        ).click()
        self.select_combobox_option(self.coe_dropdown_xpath, coe)
        sleep(1)
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='View'])[1]").click()

    def click_create_lab_button(self):
        self.logger.info("Clicking 'Create lab' button.")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.create_lab_button_xpath))).click()

    def set_date_js(self, xpath, value):
        self.logger.debug(f"Setting date '{value}' for input: {xpath}")
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        self.driver.execute_script("arguments[0].value = arguments[1];", element, value)
        self.driver.execute_script("""
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, element)

    def create_lab(self, coe, lab_name, start_time, end_time, main_mentor, support_mentor, lab_type):
        self.logger.info(f"Creating lab: {lab_name}")
        self.select_combobox_option(self.coe_select_xpath, coe)
        self.driver.find_element(By.XPATH, self.lab_name_xpath).send_keys(lab_name)
        self.driver.find_element(By.XPATH, self.session_start_xpath).send_keys(start_time)
        self.driver.find_element(By.XPATH, self.session_end_xpath).send_keys(end_time)
        self.select_combobox_option(self.main_mentor_dropdown_xpath, main_mentor)
        self.select_combobox_option(self.sub_mentor_dropdown_xpath, support_mentor)
        self.driver.find_element(By.XPATH, self.lab_type_xpath).click()
        self.driver.find_element(By.XPATH, self.click_create_xpath).click()
        sleep(3)

        assert lab_name in self.driver.page_source, "Lab not created or not displayed."
        self.logger.info(f"Lab '{lab_name}' created successfully.")

    def click_edit_newbuild_button(self):
        self.logger.info("Clicking edit button for lab.")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.edit_button_newbuild_xpath))).click()

    def delete_lab(self):
        self.logger.info("Deleting lab.")
        self.driver.find_element(By.XPATH, self.disable_lab_xpath).click()
        self.driver.find_element(By.XPATH, self.disable_confirm_xpath).click()
        self.logger.info("Lab deleted successfully.")

    def click_download_sample_lab_csv(self):
        self.logger.info("Downloading sample lab CSV.")
        download_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.download_sample_csv_xpath)))
        download_button.click()

    def edit_details(self, new_lab_name):
        self.logger.info(f"Editing lab name to: {new_lab_name}")
        details_box = self.driver.find_element(By.XPATH, self.lab_name_xpath)
        details_box.click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        sleep(2)
        details_box.send_keys(new_lab_name)
        self.driver.find_element(By.XPATH, self.update_button_xpath).click()
        sleep(3)

        assert new_lab_name in self.driver.page_source, "Lab not edited or not displayed."
        self.logger.info(f"Lab edited successfully to '{new_lab_name}'.")

    def click_download_lab_data_csv(self):
        self.logger.info("Downloading lab data CSV.")
        download_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.download_lab_data_csv_xpath)))
        download_button.click()

    def upload_lab_csv_file(self, file_path: str):
        self.logger.info(f"Uploading lab CSV from file: {file_path}")
        upload_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.upload_csv_btn_xpath)))
        upload_btn.click()
        file_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.file_input_xpath)))
        file_input.send_keys(file_path)
        sleep(5)
        submit_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.submit_csv_btn_xpath)))
        submit_btn.click()
        self.logger.info("CSV file uploaded and submitted.")
