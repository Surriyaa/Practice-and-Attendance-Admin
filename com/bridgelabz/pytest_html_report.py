# run_tests.py
import pytest
import datetime
import os

timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
report_path = f"C:/Users/ASUS/PycharmProjects/Practice-Attendance-Admin/reports/report_{timestamp}.html"

pytest.main(["testcases/test_daily_reports.py", f"--html={report_path}", "--self-contained-html"])
