import pytest
import allure
from datetime import datetime

from com.bridgelabz.pageObjects.CodeDistribution.CoderDistributionReport import CoderDistributionReport
from com.bridgelabz.testcases.conftest import take_screenshot

@allure.epic("Practice & Attendance Admin")
@allure.feature("Coder Distribution Module")
@allure.story("Validate Coder Distribution functionality")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.sanity
@pytest.mark.usefixtures("login")
class TestCoderDistribution:

    @allure.title("TestCoderDistribution::test_view_coder_distribution_report")
    @allure.story("Coder Distribution Report View Functionality")
    def test_view_coder_distribution_report(self, login, request):
        """
        Verify the Coder Distribution Report is viewed successfully and contains correct data.
        """
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id

        allure.dynamic.testcase(f"CoderDistributionReport-{tc_id}")

        try:
            report = CoderDistributionReport(login, tc_id=tc_id)
            report.view_coder_distribution_report(
                coe="P&A Phase 2",
                lab_type="Fellowship"
            )
            allure.attach("Coder Distribution Report viewed successfully", name="Coder Distribution Report", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(login, "test_view_coder_distribution_report", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"CoderDistributionReport view_coder_distribution_report failed due to: {e}")