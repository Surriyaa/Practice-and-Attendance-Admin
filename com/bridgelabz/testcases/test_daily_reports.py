import pytest

from com.bridgelabz.pageObjects.DailyReport.DailyReports import DailyReports
from com.bridgelabz.testcases.conftest import take_screenshot


@pytest.mark.usefixtures("login")
class TestDailyReports:
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