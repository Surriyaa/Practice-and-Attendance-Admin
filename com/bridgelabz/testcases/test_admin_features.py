import os
from datetime import time
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.bridgelabz.pageObjects.LabPractice.LabPractice import LabPractice
from com.bridgelabz.testcases.conftest import take_screenshot

from com.bridgelabz.pageObjects.CheckInOutReport.CheckInOutReport import CheckInOutReport
from com.bridgelabz.pageObjects.CodeDistribution.CoderDistributionReport import CoderDistributionReport
from com.bridgelabz.pageObjects.DailyReport.DailyReports import DailyReports
from com.bridgelabz.pageObjects.LabReport.LabReport import LabReports
from com.bridgelabz.pageObjects.MakerPlan.MakerPlanPage import MakerPlanPage
from com.bridgelabz.pageObjects.PracticeHead.PracticeHead import PHPage
from com.bridgelabz.pageObjects.PracticeMentor.PracticeMentorPage import MentorPage

@pytest.mark.usefixtures("login")
class TestAdminFeatures:
    @pytest.mark.sanity
    def test_create_maker_plan(self, login):
        try:
            maker = MakerPlanPage(login)
            sleep(5)
            maker.create_maker_plan("Full Stack Testing 3", "88", description="This is An Automated Description 01")
        except Exception as e:
            take_screenshot(login, "test_create_maker_plan")
            raise e

    @pytest.mark.sanity
    def test_edit_maker_plan(self, login):
        try:
            maker = MakerPlanPage(login)
            maker.edit_module_in_plan("P & A Phase 2", "78")
        except Exception as e:
            take_screenshot(login, "test_edit_maker_plan")
            raise e

    @pytest.mark.sanity
    def test_create_ph(self, login):
        try:
            ph = PHPage(login)
            ph.create_ph("Surriyaa sanity2", "surriyaatestsanity2@gmail.com", 6374400001, "P&A Phase 2")
        except Exception as e:
            take_screenshot(login, "test_create_ph")
            raise e

    @pytest.mark.sanity
    def test_edit_ph(self, login):
        try:
            ph = PHPage(login)
            ph.edit_ph_contact("9918001191")
        except Exception as e:
            take_screenshot(login, "test_edit_ph")
            raise e

    @pytest.mark.sanity
    def test_create_mentor(self, login):
        try:
            mentor = MentorPage(login)
            mentor.create_practice_mentor("Surriyaa sanity3", "surriysanity2@bridgelabz.com", "6374670107", "P&A Phase 2")
        except Exception as e:
            take_screenshot(login, "test_create_mentor")
            raise e

    @pytest.mark.sanity
    def test_edit_mentor(self, login):
        try:
            mentor = MentorPage(login)
            mentor.edit_mentor_contact("9876522621")
        except Exception as e:
            take_screenshot(login, "test_edit_mentor")
            raise e

    @pytest.mark.sanity
    def test_view_daily_attendance_report(self, login):
        try:
            reports = DailyReports(login)
            reports.view_daily_attendance_report(
                coe="P&A Phase 2",
                lab_type="Fellowship",
                attendance="Day Order1",
                session="10:00 AM - 05:00 PM",
                from_date="2025-05-01",
                to_date="2025-07-01"
            )
        except Exception as e:
            take_screenshot(login, "test_view_daily_attendance_report")
            raise e

    @pytest.mark.sanity
    def test_view_daily_practice_report(self, login):
        try:
            reports = DailyReports(login)
            reports.view_daily_practice_report(
                coe="P&A Phase 2",
                lab_type="Fellowship",
                maker_plan="java programming",
                maker_module="CodInClub @Java - Core Programming",
                lab="Lab 1"
            )
        except Exception as e:
            take_screenshot(login, "test_view_daily_practice_report")
            raise e

    @pytest.mark.sanity
    def test_lab_reports(self, login):
        try:
            reports = LabReports(login)
            reports.view_lab_report()
        except Exception as e:
            take_screenshot(login, "test_lab_reports")
            raise e

    @pytest.mark.sanity
    def test_view_coder_distribution_report(self, login):
        try:
            report = CoderDistributionReport(login)
            report.view_coder_distribution_report(
                coe="P&A Phase 2",
                lab_type="Fellowship"
            )
        except Exception as e:
            take_screenshot(login, "test_view_coder_distribution_report")
            raise e

    @pytest.mark.sanity
    def test_view_checkin_checkout_report(self, login):
        try:
            check_in_out = CheckInOutReport(login)
            check_in_out.view_checkin_checkout_report(
                coe="P&A Phase 2",
                lab_type="Fellowship",
                attendance_name="July 16",
                session_time="10:00 AM - 04:00 PM",
                from_date="2025-05-01",
                to_date="2025-07-01"
            )
        except Exception as e:
            take_screenshot(login, "test_view_checkin_checkout_report")
            raise e

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
        practice = LabPractice(login)

        download_directory = os.path.expanduser("~/Downloads")
        expected_file_prefix = "SampleLearnerCSV"
        file_extension = ".csv"
        wait_timeout = 10

        # Clean existing files
        for file in os.listdir(download_directory):
            if file.startswith(expected_file_prefix) and file.endswith(file_extension):
                os.remove(os.path.join(download_directory, file))

        # Perform UI actions
        practice.select_coe("P&A Phase 2")
        practice.click_download_sample_lab_csv()
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
        practice = LabPractice(driver)

        download_directory = os.path.expanduser("~/Downloads")
        expected_file_prefix = "LearnersData"
        file_extension = ".csv"
        wait_timeout = 10

        # Clean existing files
        for file in os.listdir(download_directory):
            if file.startswith(expected_file_prefix) and file.endswith(file_extension):
                os.remove(os.path.join(download_directory, file))

        # Perform UI actions
        practice.select_coe("P&A Phase 2")
        practice.click_download_lab_data_csv()
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

    @pytest.mark.csv
    def test_upload_csv_file(self, login):
        driver = login
        practice = LabPractice(driver)
        # Ensure file path is correct
        file_path = r"C:\Users\ASUS\Downloads\SampleLearnerCSV.csv"  # <-- FIXED
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
