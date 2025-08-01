import pytest
import datetime

# Generate dynamic report name using current timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_file = f"C:/Users/ASUS/PycharmProjects/Practice-Attendance-Admin/reports/sanity_report_{timestamp}.html"

# Run sanity tests with dynamic HTML report generation
exit_code = pytest.main([
    "-m", "sanity",
    "--html", report_file,
    "--self-contained-html"
])

# Optional: Exit with the same code as pytest
exit(exit_code)
