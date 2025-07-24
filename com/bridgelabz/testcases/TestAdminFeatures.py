from time import sleep
import pytest

from com.bridgelabz.pageObjects.CheckInOutReport.CheckInOutReport import CheckInOutReport
from com.bridgelabz.pageObjects.CodeDistribution.CoderDistributionReport import CoderDistributionReport
from com.bridgelabz.pageObjects.DailyReport.DailyReports import DailyReports
from com.bridgelabz.pageObjects.LabReport.LabReport import LabReports
from com.bridgelabz.pageObjects.MakerPlan.MakerPlanPage import MakerPlanPage
from com.bridgelabz.pageObjects.PracticeHead.PracticeHead import PHPage
from com.bridgelabz.pageObjects.PracticeMentor.PracticeMentorPage import MentorPage


@pytest.mark.usefixtures("login")
class TestAdminFeatures:

    def test_create_maker_plan(self, login):
        maker = MakerPlanPage(login)
        sleep(5)
        maker.create_maker_plan("Full Stack Dev", "60", description="This is An Automated Description")

    def test_edit_maker_plan(self, login):
        maker = MakerPlanPage(login)
        maker.edit_module_in_plan("P & A Phase 2", "80")

    def test_create_ph(self, login):
        ph = PHPage(login)
        ph.create_ph("Surriyaa 2", "surriyaatest1@gmail.com", 6374637402, "P&A Phase 2")

    def test_edit_ph(self, login):
        ph = PHPage(login)
        ph.edit_ph_contact("9988000000")

    def test_create_mentor(self, login):
        mentor = MentorPage(login)
        mentor.create_practice_mentor("Surriyaa Test1", "surriy66@bridgelabz.com", "6374674463", "P&A Phase 2")

    def test_edit_mentor(self, login):
        mentor = MentorPage(login)
        mentor.edit_mentor_contact("9876540000")

    def test_view_daily_attendance_report(self, login):
        reports = DailyReports(login)

        # Test Daily Attendance Report
        reports.view_daily_attendance_report(
            coe="P&A Phase 2",
            lab_type="Fellowship",
            attendance="Day Order1",
            session="10:00 AM - 05:00 PM",
            from_date="01-05-2025",  # Correct format: yyyy-mm-dd
            to_date="2025-07-01"  # Correct format: yyyy-mm-dd
        )

    def test_view_daily_practice_report(self, login):
        reports = DailyReports(login)

        # Test Daily Practice Report
        reports.view_daily_practice_report(
            coe="P&A Phase 2",
            lab_type="Fellowship",
            maker_plan="java programming",
            maker_module="CodInClub @Java - Core Programming",
            lab="Lab 1"
        )

    def test_lab_reports(self, login):
        reports = LabReports(login)

        reports.view_lab_report()

    def test_view_coder_distribution_report(self, login):
        report = CoderDistributionReport(login)

        report.view_coder_distribution_report(
            coe="P&A Phase 2",
            lab_type="Fellowship"
        )

    def test_view_checkin_checkout_report(self, login):
        check_in_out = CheckInOutReport(login)

        check_in_out.view_checkin_checkout_report(
            coe="P&A Phase 2",
            lab_type="Fellowship",
            attendance_name="July 16",
            session_time="10:00 AM - 04:00 PM",
            from_date="2025-05-01",  # Correct format: yyyy-mm-dd
            to_date="2025-07-01"  # Correct format: yyyy-mm-dd
        )
