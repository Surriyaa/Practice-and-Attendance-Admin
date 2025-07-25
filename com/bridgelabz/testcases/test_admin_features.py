from time import sleep
import pytest
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
