import pytest

from com.bridgelabz.pageObjects.LabReport.LabReport import LabReports
from com.bridgelabz.testcases.conftest import take_screenshot


@pytest.mark.usefixtures("login")
class TestLabReports:
    @pytest.mark.sanity
    def test_lab_reports(self, login):
        try:
            reports = LabReports(login)
            reports.view_lab_report()
        except Exception as e:
            take_screenshot(login, "test_lab_reports")
            raise e