import pytest
import allure
from datetime import datetime

from com.bridgelabz.pageObjects.CheckInOutReport.CheckInOutReport import CheckInOutReport
from com.bridgelabz.testcases.conftest import take_screenshot

@allure.epic("Practice & Attendance Admin")
@allure.feature("CheckIn-Out Reports Module")
@allure.story("Validate CheckIn-Out Reports functionality")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.sanity
@pytest.mark.usefixtures("login")
class TestCheckinOutReport:

    @allure.title("TestCheckinOutReport::test_view_checkin_checkout_report")
    @allure.story("CheckIn-Out Report View Functionality")
    def test_view_checkin_checkout_report(self, login, request):
        """
        Verify the CheckIn-Out Report is viewed successfully and contains correct data.
        """
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id

        allure.dynamic.testcase(f"CheckInOutReport-{tc_id}")

        try:
            check_in_out = CheckInOutReport(login, tc_id=tc_id)
            check_in_out.view_checkin_checkout_report(
                coe="P&A Phase 2",
                lab_type="Fellowship",
                attendance_name="July 16",
                session_time="10:00 AM - 04:00 PM",
                from_date="2025-05-01",
                to_date="2025-07-01"
            )
            allure.attach("CheckIn-Out Report viewed successfully", name="CheckInOut Report", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(login, "test_view_checkin_checkout_report", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"CheckInOutReport view_checkin_checkout_report failed due to: {e}")