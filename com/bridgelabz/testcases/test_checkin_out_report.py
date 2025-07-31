import pytest

from com.bridgelabz.pageObjects.CheckInOutReport.CheckInOutReport import CheckInOutReport
from com.bridgelabz.testcases.conftest import take_screenshot


@pytest.mark.usefixtures("login")
class TestCheckinOutReport:
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