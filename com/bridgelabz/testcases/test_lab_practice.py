from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.bridgelabz.pageObjects.LabPractice.LabPractice import LabPractice
from com.bridgelabz.testcases.conftest import take_screenshot

import os
import time


def delete_existing_sample_csv(download_dir, file_prefix, file_ext):
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

@pytest.mark.usefixtures("login")
class TestLabPractice:

    @pytest.mark.sanity
    def test_create_lab_practice(self, login):
        try:
            practice = LabPractice(login)
            practice.select_coe("P&A Phase 2")
            practice.click_create_lab_button()
            practice.create_lab("P&A Phase 2",
                                "Automation Testing",
                                "10:00AM",
                                "05:00PM",
                                "surriyaa.pp@bridgelabz.com",
                                "surriysanity2@bridgelabz.com",
                                "Fellowship")
        except Exception as e:
            take_screenshot(login, "test_create_lab_practice")
            raise e

    @pytest.mark.sanity
    def test_edit_lab_practice(self, login):
        try:
            practice = LabPractice(login)
            practice.select_coe("P&A Phase 2")
            practice.click_edit_newbuild_button()
            practice.edit_details("Edited Lab Name")
        except Exception as e:
            take_screenshot(login, "test_edit_lab_practice")
            raise e

    @pytest.mark.sanity
    def test_check_download_sample_lab__csv(self, login):
        driver = login
        practice = LabPractice(driver)

        download_directory = os.path.expanduser("~/Downloads")
        expected_file_prefix = "SampleLabCSV"
        file_extension = ".csv"
        wait_timeout = 10

        # Step 1: Delete existing files
        delete_existing_sample_csv(download_directory, expected_file_prefix, file_extension)

        # Step 2: Perform UI actions
        practice.select_coe("P&A Phase 2")
        practice.click_download_sample_lab_csv()
        sleep(2)

        # Step 3: Verify toast
        toast_xpath = "//*[contains(text(),'downloaded successfully')]"
        try:
            WebDriverWait(driver, wait_timeout).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            print("Toast message verified: File downloaded successfully.")
        except Exception as e:
            take_screenshot(driver, "test_check_download_sample_csv_toast_fail")
            raise AssertionError("Toast message not found or text mismatch. " + str(e))

        # Step 4: Verify file downloaded
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
            print(f"CSV file downloaded successfully: {downloaded_file_path}")
        else:
            take_screenshot(driver, "test_check_download_sample_csv_file_fail")
            raise AssertionError("CSV file not downloaded in Downloads folder.")

    @pytest.mark.sanity
    def test_check_download_learner_data_csv(self, login):
        driver = login
        practice = LabPractice(driver)

        download_directory = os.path.expanduser("~/Downloads")
        expected_file_prefix = "LabData"
        file_extension = ".csv"
        wait_timeout = 10

        # Clean existing files
        for file in os.listdir(download_directory):
            if file.startswith(expected_file_prefix) and file.endswith(file_extension):
                os.remove(os.path.join(download_directory, file))

        # Perform UI actions
        practice.select_coe("P&A Phase 2")
        practice.click_download_lab_data_csv()
        sleep(2)

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
                sleep(1)

            assert file_downloaded, "CSV file not downloaded in Downloads folder."
            print(f"CSV file downloaded successfully.")
        except Exception as e:
            take_screenshot(driver, "test_check_download_sample_csv_file_fail")
            raise AssertionError("CSV file download verification failed. " + str(e))

    @pytest.mark.csv
    def test_upload_csv_file(self, login):
        driver = login
        practice = LabPractice(driver)
        # Ensure file path is correct
        file_path = r"C:\Users\ASUS\Downloads\SampleLabCSV.csv"  # <-- FIXED
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV file not found at: {file_path}")

        practice.select_coe("P&A Phase 2")
        practice.upload_lab_csv_file(file_path=file_path)

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

    @pytest.mark.regular
    def test_disable_lab(self, login):
        driver = login
        practice = LabPractice(driver)
        practice.select_coe("P&A Phase 2")
        practice.delete_lab()
        sleep(1)

        # Verify toaster message
        toast_xpath = "//*[contains(text(),'deactivated successfully')]"

        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            print("Toast message verified: File deactivated successfully.")
        except Exception as e:
            take_screenshot(driver, "test_delete_lab_toast_fail")
            raise AssertionError("Toast message not found or text mismatch. " + str(e))