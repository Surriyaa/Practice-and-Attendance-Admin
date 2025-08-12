import pytest
import datetime
import os
import subprocess

# Generate dynamic folder name for Allure results
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
results_dir = f"C:/Users/ASUS/PycharmProjects/Practice-Attendance-Admin/reports/allure_results_{timestamp}"
report_dir = f"C:/Users/ASUS/PycharmProjects/Practice-Attendance-Admin/reports/allure_report_{timestamp}"

# 1️⃣ Run pytest with Allure results output
exit_code = pytest.main([
    "-m", "sanity",
    f"--alluredir={results_dir}"
])

# 2️⃣ Generate the Allure HTML report
subprocess.run(["allure", "generate", results_dir, "-o", report_dir, "--clean"], shell=True)

print(f"✅ Allure report generated at: {report_dir}")

# 3️⃣ Exit with pytest's exit code
exit(exit_code)
