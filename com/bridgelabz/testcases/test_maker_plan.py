import pytest
import allure
from datetime import datetime

from com.bridgelabz.pageObjects.DailyReport.DailyReports import DailyReports
from com.bridgelabz.testcases.conftest import take_screenshot

@allure.epic("Practice & Attendance Admin")
@allure.feature("Daily Reports Module")
@allure.story("Validate Daily Reports functionality")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.sanity
@pytest.mark.usefixtures("login")
class TestDailyReports:

    @allure.title("TestDailyReports::test_view_daily_attendance_report")
    @allure.story("Daily Attendance Report View Functionality")
    def test_view_daily_attendance_report(self, login, request):
        """
        Verify the Daily Attendance Report is viewed successfully and contains correct data.
        """
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id

        allure.dynamic.testcase(f"DailyAttendanceReport-{tc_id}")

        try:
            reports = DailyReports(login, tc_id=tc_id)
            reports.view_daily_attendance_report(
                coe="P&A Phase 2",
                lab_type="Fellowship",
                attendance="Day Order1",
                session="10:00 AM - 05:00 PM",
                from_date="2025-05-01",
                to_date="2025-07-01"
            )
            allure.attach("Daily Attendance Report viewed successfully", name="Attendance Report", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(login, "test_view_daily_attendance_report", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"DailyReports view_daily_attendance_report failed due to: {e}")

    @allure.title("TestDailyReports::test_view_daily_practice_report")
    @allure.story("Daily Practice Report View Functionality")
    def test_view_daily_practice_report(self, login, request):
        """
        Verify the Daily Practice Report is viewed successfully and contains correct data.
        """
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id

        allure.dynamic.testcase(f"DailyPracticeReport-{tc_id}")

        try:
            reports = DailyReports(login, tc_id=tc_id)
            reports.view_daily_practice_report(
                coe="P&A Phase 2",
                lab_type="Fellowship",
                maker_plan="QA",
                maker_module="QA Automation",
                lab="Lab 1"
            )
            allure.attach("Daily Practice Report viewed successfully", name="Practice Report", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(login, "test_view_daily_practice_report", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"DailyReports view_daily_practice_report failed due to: {e}")