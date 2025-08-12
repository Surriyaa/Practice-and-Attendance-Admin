import pytest
import allure
from time import sleep
import os
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.bridgelabz.pageObjects.LabPractice.LabPractice import LabPractice
from com.bridgelabz.testcases.conftest import take_screenshot

@allure.epic("Practice & Attendance Admin")
@allure.feature("Lab Practice Module")
@allure.story("Validate Lab Practice functionality")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login")
class TestLabPractice:

    def delete_existing_sample_csv(self, download_dir, file_prefix, file_ext):
        deleted = False
        for file in os.listdir(download_dir):
            file_path = os.path.join(download_dir, file)
            if file.startswith(file_prefix) and file.endswith(file_ext):
                try:
                    os.remove(file_path)
                    print(f"Deleted old file: {file_path}")
                    deleted = True
                except Exception as e:
                    print(f"Could not delete file: {file_path}. Reason: {e}")
        if not deleted:
            print("No old sample CSV found to delete.")

    @allure.title("TestLabPractice::test_create_lab_practice")
    @allure.story("Create Lab Practice Functionality")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_create_lab_practice(self, login, request):
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id
        allure.dynamic.testcase(f"LabPracticeCreate-{tc_id}")
        try:
            practice = LabPractice(login, tc_id=tc_id)
            practice.select_coe("P&A Phase 2")
            practice.click_create_lab_button()
            lab_name = f"RandomLab{int(time.time())}"
            practice.create_lab("P&A Phase 2",
                                lab_name,
                                "10:00AM",
                                "05:20PM",
                                3,2025,
                                "surriyaa.pp@bridgelabz.com",
                                "surriyaa@gmail.com",
                                "Fellowship")
            allure.attach("Lab Practice created successfully", name="Create Lab", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(login, "test_create_lab_practice", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"LabPractice create_lab failed due to: {e}")

    @allure.title("TestLabPractice::test_edit_lab_practice")
    @allure.story("Edit Lab Practice Functionality")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_edit_lab_practice(self, login, request):
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id
        allure.dynamic.testcase(f"LabPracticeEdit-{tc_id}")
        try:
            practice = LabPractice(login, tc_id=tc_id)
            practice.select_coe("P&A Phase 2")
            practice.click_edit_newbuild_button()
            practice.edit_details("Edited Lab Name-1")
            allure.attach("Lab Practice edited successfully", name="Edit Lab", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(login, "test_edit_lab_practice", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"LabPractice edit_details failed due to: {e}")

    @allure.title("TestLabPractice::test_check_download_sample_lab_csv")
    @allure.story("Sample Lab CSV Download Functionality")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_check_download_sample_lab__csv(self, login, request):
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id
        allure.dynamic.testcase(f"SampleLabCSVDownload-{tc_id}")
        driver = login
        practice = LabPractice(driver, tc_id=tc_id)

        download_directory = os.path.expanduser("~/Downloads")
        expected_file_prefix = "SampleLabCSV"
        file_extension = ".csv"
        wait_timeout = 10

        self.delete_existing_sample_csv(download_directory, expected_file_prefix, file_extension)

        practice.select_coe("P&A Phase 2")
        practice.click_download_sample_lab_csv()
        sleep(2)

        toast_xpath = "//*[contains(text(),'downloaded successfully')]"
        try:
            WebDriverWait(driver, wait_timeout).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            allure.attach("Toast message verified: File downloaded successfully.", name="Sample CSV Download", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(driver, "test_check_download_sample_csv_toast_fail", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("Toast message not found or text mismatch. " + str(e))

        file_downloaded = False
        end_time = time.time() + wait_timeout
        downloaded_file_path = ""

        while time.time() < end_time:
            for file in os.listdir(download_directory):
                if file.startswith(expected_file_prefix) and file.endswith(file_extension):
                    file_downloaded = True
                    downloaded_file_path = os.path.join(download_directory, file)
                    break
            if file_downloaded:
                break
            sleep(1)

        if file_downloaded:
            allure.attach(f"CSV file downloaded successfully: {downloaded_file_path}", name="Sample CSV File", attachment_type=allure.attachment_type.TEXT)
        else:
            take_screenshot(driver, "test_check_download_sample_csv_file_fail", tc_id=tc_id)
            allure.attach("CSV file not downloaded in Downloads folder.", name="Sample CSV File", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("CSV file not downloaded in Downloads folder.")

    @allure.title("TestLabPractice::test_check_download_learner_data_csv")
    @allure.story("Learner Data CSV Download Functionality")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_check_download_learner_data_csv(self, login, request):
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id
        allure.dynamic.testcase(f"LearnerDataCSVDownload-{tc_id}")
        driver = login
        practice = LabPractice(driver, tc_id=tc_id)

        download_directory = os.path.expanduser("~/Downloads")
        expected_file_prefix = "LabData"
        file_extension = ".csv"
        wait_timeout = 10

        for file in os.listdir(download_directory):
            if file.startswith(expected_file_prefix) and file.endswith(file_extension):
                os.remove(os.path.join(download_directory, file))

        practice.select_coe("P&A Phase 2")
        practice.click_download_lab_data_csv()
        sleep(2)

        toast_xpath = "//*[contains(text(),'downloaded successfully')]"

        try:
            WebDriverWait(driver, wait_timeout).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            allure.attach("Toast message verified: File downloaded successfully.", name="Learner Data CSV Download", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(driver, "test_check_download_sample_csv_toast_fail", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("Toast message not found or text mismatch. " + str(e))

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
                sleep(1)

            assert file_downloaded, "CSV file not downloaded in Downloads folder."
            allure.attach(f"CSV file downloaded successfully: {downloaded_file_path}", name="Learner Data CSV File", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(driver, "test_check_download_sample_csv_file_fail", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("CSV file download verification failed. " + str(e))

    @allure.title("TestLabPractice::test_upload_csv_file")
    @allure.story("Lab CSV Upload Functionality")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_upload_csv_file(self, login, request):
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id
        allure.dynamic.testcase(f"LabCSVUpload-{tc_id}")
        driver = login
        practice = LabPractice(driver, tc_id=tc_id)
        file_path = r"C:/Users/ASUS/Downloads/CSVFiles/SampleLabCSV.csv"
        if not os.path.exists(file_path):
            allure.attach(f"CSV file not found at: {file_path}", name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"CSV file not found at: {file_path}")

        practice.select_coe("P&A Phase 2")
        practice.upload_lab_csv_file(file_path=file_path)

        toast_xpath = "//*[contains(text(),'Upload complete')]"
        try:
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            allure.attach("Toast message verified: File upload successfully.", name="Upload Lab CSV", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(driver, "upload_csv_file", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("Toast message not found or mismatch. " + str(e))

    @allure.title("TestLabPractice::test_disable_lab")
    @allure.story("Disable Lab Functionality")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regular
    def test_disable_lab(self, login, request):
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id
        allure.dynamic.testcase(f"LabDisable-{tc_id}")
        driver = login
        practice = LabPractice(driver, tc_id=tc_id)
        practice.select_coe("P&A Phase 2")
        practice.delete_lab()
        sleep(1)

        toast_xpath = "//*[contains(text(),'deactivated successfully')]"

        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            allure.attach("Toast message verified: Lab deactivated successfully.", name="Disable Lab", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(driver, "test_delete_lab_toast_fail", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("Toast message not found or text mismatch. " + str(e))