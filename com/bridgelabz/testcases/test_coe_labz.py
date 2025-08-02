import os
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.bridgelabz.pageObjects.COELabs.COELabs import COELabs
from com.bridgelabz.testcases.conftest import take_screenshot

@pytest.mark.usefixtures("login")
class TestCOE:
    # Test Data
    COE_NAME = "Automation COE-8"
    COE_DETAILS = "Automation Testing-8"
    LATITUDE = "19.135420"
    LONGITUDE = "72.54894"
    DISTANCE = "500"
    EDITED_DETAILS = "SRM TN Updated Automation 3"

    @pytest.mark.sanity
    def test_create_coe(self, login):
        driver = login
        coe = COELabs(driver)

        try:
            coe.click_create_coe_button()
            coe.fill_create_coe_form(
                self.COE_NAME,
                self.COE_DETAILS,
                self.LATITUDE,
                self.LONGITUDE,
                self.DISTANCE
            )
            coe.click_create_button()

            assert self.COE_NAME in driver.page_source, "COE creation failed"
            print(f"COE Creation successful: '{self.COE_NAME}' found in page source")
        except Exception as e:
            take_screenshot(driver, "test_create_coe")
            raise AssertionError("COE creation failed. " + str(e))

    @pytest.mark.sanity
    def test_edit_coe(self, login):
        driver = login
        coe = COELabs(driver)

        try:
            coe.click_edit_SRMTN_button()
            coe.edit_details(self.EDITED_DETAILS)
            coe.click_edit_button()

            assert self.EDITED_DETAILS in driver.page_source, "COE edit failed"
            print(f"COE Edit successful: '{self.EDITED_DETAILS}' found in page source")
        except Exception as e:
            take_screenshot(driver, "test_edit_coe")
            raise AssertionError("COE edit failed. " + str(e))

    @pytest.mark.regular
    def test_disable_coe(self, login):
        driver = login
        coe = COELabs(driver)

        coe.click_disable_button()

        try:
            toast_xpath = "//*[contains(text(),'disabled successfully')]"
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            print("COE disabled Successfully.")
        except Exception as e:
            take_screenshot(driver, "test_disable_coe")
            raise AssertionError(f"COE disabling failed. Reason: {str(e)}")

    @pytest.mark.sanity
    def test_check_download_sample_csv(self, login):
        driver = login
        coe = COELabs(driver)

        download_directory = os.path.expanduser("~/Downloads")
        expected_file_prefix = "SampleLearnerCSV"
        file_extension = ".csv"
        wait_timeout = 10

        # Clean existing files
        for file in os.listdir(download_directory):
            if file.startswith(expected_file_prefix) and file.endswith(file_extension):
                os.remove(os.path.join(download_directory, file))

        # Perform UI actions
        coe.click_learner_button()
        coe.click_download_learner_data_csv()
        time.sleep(2)

        # Verify toaster message
        toast_xpath = "//*[contains(text(),'downloaded successfully')]"

        try:
            WebDriverWait(driver, wait_timeout).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            print("Toast message verified: File downloaded successfully.")
        except Exception as e:
            take_screenshot(driver, "test_check_download_sample_csv_toast_fail")
            raise AssertionError("Toast message not found or text mismatch. " + str(e))

        # Check file downloaded
        file_downloaded = False
        end_time = time.time() + wait_timeout

        try:
            while time.time() < end_time:
                for file in os.listdir(download_directory):
                    if file.startswith(expected_file_prefix) and file.endswith(file_extension):
                        file_downloaded = True
                        downloaded_file_path = os.path.join(download_directory, file)
                        break
                if file_downloaded:
                    break
                time.sleep(1)

            assert file_downloaded, "CSV file not downloaded in Downloads folder."
            print(f"CSV file downloaded successfully.")
        except Exception as e:
            take_screenshot(driver, "test_check_download_sample_csv_file_fail")
            raise AssertionError("CSV file download verification failed. " + str(e))

    @pytest.mark.sanity
    def test_check_download_learner_data_csv(self, login):
        driver = login
        coe = COELabs(driver)

        download_directory = os.path.expanduser("~/Downloads")
        expected_file_prefix = "LearnersData"
        file_extension = ".csv"
        wait_timeout = 10

        # Clean existing files
        for file in os.listdir(download_directory):
            if file.startswith(expected_file_prefix) and file.endswith(file_extension):
                os.remove(os.path.join(download_directory, file))

        # Perform UI actions
        coe.click_learner_button()
        coe.click_download_learner_data_csv()
        time.sleep(2)

        # Verify toaster message
        toast_xpath = "//*[contains(text(),'downloaded successfully')]"

        try:
            WebDriverWait(driver, wait_timeout).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            print("Toast message verified: File downloaded successfully.")
        except Exception as e:
            take_screenshot(driver, "test_check_download_sample_csv_toast_fail")
            raise AssertionError("Toast message not found or text mismatch. " + str(e))

        # Check file downloaded
        file_downloaded = False
        end_time = time.time() + wait_timeout

        try:
            while time.time() < end_time:
                for file in os.listdir(download_directory):
                    if file.startswith(expected_file_prefix) and file.endswith(file_extension):
                        file_downloaded = True
                        downloaded_file_path = os.path.join(download_directory, file)
                        break
                if file_downloaded:
                    break
                time.sleep(1)

            assert file_downloaded, "CSV file not downloaded in Downloads folder."
            print(f"CSV file downloaded successfully.")
        except Exception as e:
            take_screenshot(driver, "test_check_download_learner_data_csv_file_fail")
            raise AssertionError("CSV file download verification failed. " + str(e))

    @pytest.mark.sanity
    def test_upload_csv_file(self, login):
        driver = login
        coe = COELabs(driver)

        # Ensure file path is correct
        file_path = r"C:\Users\ASUS\Downloads\CSVFiles\SampleLearnerCSV.csv"  # <-- FIXED
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV file not found at: {file_path}")

        coe.click_learner_button()
        coe.upload_csv_file(file_path=file_path)

        # Verify success toast
        toast_xpath = "//*[contains(text(),'successfully')]"
        try:
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            print("Toast message verified: File upload successfully.")
        except Exception as e:
            take_screenshot(driver, "upload_csv_file")
            raise AssertionError("Toast message not found or mismatch. " + str(e))

