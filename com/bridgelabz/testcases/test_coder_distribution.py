import pytest

from com.bridgelabz.pageObjects.CodeDistribution.CoderDistributionReport import CoderDistributionReport
from com.bridgelabz.testcases.conftest import take_screenshot


@pytest.mark.usefixtures("login")
class TestCoderDistribution:
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