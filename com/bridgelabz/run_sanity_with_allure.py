import os
import time
import subprocess

# Step 1: Run pytest with sanity marker
subprocess.run([
    "pytest", "-m", "sanity",
    "--alluredir=reports/allure_results"
], check=True)

# Step 2: Create timestamped report directory
timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
report_dir = f"C:/Users/ASUS/PycharmProjects/Practice-Attendance-Admin/com/bridgelabz/utilities/reports/allure_report_sanity_{timestamp}"

# Step 3: Generate Allure HTML report
subprocess.run([
    "allure", "generate", "reports/allure_results",
    "-o", report_dir, "--clean"
], check=True)

# Step 4: Open the Allure report in browser
subprocess.run(["allure", "open", report_dir], check=True)
