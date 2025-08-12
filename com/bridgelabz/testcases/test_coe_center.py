import os
import time
import pytest
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.bridgelabz.pageObjects.COECenter.COECenter import COECenter
from com.bridgelabz.testcases.conftest import take_screenshot

@allure.epic("Practice & Attendance Admin")
@allure.feature("COE Center Module")
@allure.story("Validate COE Center functionality")
@pytest.mark.usefixtures("login")
class TestCOE:

    COE_NAME = f"RandomCOE{int(time.time())}"
    COE_DETAILS = "Automation Testing-9"
    LATITUDE = "19.135420"
    LONGITUDE = "72.54894"
    DISTANCE = "350"
    EDITED_DETAILS = "SRM TN Updated Automation 3"

    @allure.title("TestCOE::test_create_coe")
    @allure.story("COE Creation Functionality")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_create_coe(self, login, request):
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id
        allure.dynamic.testcase(f"COECreation-{tc_id}")
        driver = login
        coe = COECenter(driver, tc_id=tc_id)
        try:
            coe.click_coe_center_tab()
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
            allure.attach(f"COE '{self.COE_NAME}' created successfully", name="COE Creation", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(driver, "test_create_coe", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"COE creation failed. {e}")

    @allure.title("TestCOE::test_edit_coe")
    @allure.story("COE Edit Functionality")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_edit_coe(self, login, request):
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id
        allure.dynamic.testcase(f"COEEdit-{tc_id}")
        driver = login
        coe = COECenter(driver, tc_id=tc_id)
        try:
            coe.click_coe_center_tab()
            coe.click_edit_SRMTN_button()
            coe.edit_details(self.EDITED_DETAILS)
            coe.click_edit_button()
            assert self.EDITED_DETAILS in driver.page_source, "COE edit failed"
            allure.attach(f"COE edited successfully: '{self.EDITED_DETAILS}'", name="COE Edit", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(driver, "test_edit_coe", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"COE edit failed. {e}")

    @allure.title("TestCOE::test_disable_coe")
    @allure.story("COE Disable Functionality")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regular
    def test_disable_coe(self, login, request):
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id
        allure.dynamic.testcase(f"COEDisable-{tc_id}")
        driver = login
        coe = COECenter(driver, tc_id=tc_id)
        coe.click_coe_center_tab()
        coe.click_disable_button()
        toast_xpath = "//*[contains(text(),'disabled successfully')]"
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            allure.attach("COE disabled Successfully.", name="COE Disable", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(driver, "test_disable_coe", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"COE disabling failed. Reason: {e}")

    @allure.title("TestCOE::test_check_download_sample_csv")
    @allure.story("Sample CSV Download Functionality")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_check_download_sample_csv(self, login, request):
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id
        allure.dynamic.testcase(f"COESampleCSVDownload-{tc_id}")
        driver = login
        coe = COECenter(driver, tc_id=tc_id)
        download_directory = os.path.expanduser("~/Downloads")
        expected_file_prefix = "SampleLearnerCSV"
        file_extension = ".csv"
        wait_timeout = 10

        for file in os.listdir(download_directory):
            if file.startswith(expected_file_prefix) and file.endswith(file_extension):
                os.remove(os.path.join(download_directory, file))

        coe.click_coe_center_tab()
        coe.click_learner_button()
        coe.click_download_sample_csv()
        time.sleep(2)
        toast_xpath = "//*[contains(text(),'downloaded successfully')]"
        try:
            WebDriverWait(driver, wait_timeout).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            allure.attach("Toast message verified: File downloaded successfully.", name="Sample CSV Download", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(driver, "test_check_download_sample_csv_toast_fail", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"Toast message not found or text mismatch. {e}")

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
        # Generate TC_ID based on current seconds: "TC_<1–25>"
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        driver = login
        coe = COECenter(driver, tc_id=tc_id)

        download_directory = os.path.expanduser("~/Downloads")
        expected_file_prefix = "LearnersData"
        file_extension = ".csv"
        wait_timeout = 10

        # Clean existing files
        for file in os.listdir(download_directory):
            if file.startswith(expected_file_prefix) and file.endswith(file_extension):
                os.remove(os.path.join(download_directory, file))

        # Perform UI actions
        coe.click_coe_center_tab()
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
        # Generate TC_ID based on current seconds: "TC_<1–25>"
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        driver = login
        coe = COECenter(driver, tc_id=tc_id)

        # Ensure file path is correct
        file_path = r"C:\Users\ASUS\Downloads\CSVFiles\SampleLearnerCSV.csv"  # <-- FIXED
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV file not found at: {file_path}")

        coe.click_coe_center_tab()
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