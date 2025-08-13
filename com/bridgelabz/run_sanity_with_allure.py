import subprocess
import time
import os

try:
    # ✅ Single folder for results — no mismatch
    allure_results_dir = r"C:/Users/ASUS/PycharmProjects/Practice-Attendance-Admin/reports/allure_results"

    # Ensure folder exists & is empty
    if os.path.exists(allure_results_dir):
        for file in os.listdir(allure_results_dir):
            os.remove(os.path.join(allure_results_dir, file))
    else:
        os.makedirs(allure_results_dir)

    # ✅ Step 1 – Run pytest with sanity marker
    subprocess.run([
        "pytest",
        r"C:/Users/ASUS/PycharmProjects/Practice-Attendance-Admin/com/bridgelabz/testcases/test_lab_reports.py",
        "-m", "sanity",
        f"--alluredir={allure_results_dir}"
    ], check=False)  # ❌ no check=True so script continues even if tests fail

finally:
    # ✅ Step 2 – Generate timestamped report folder
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = fr"C:/Users/ASUS/PycharmProjects/Practice-Attendance-Admin/reports/allure_report_sanity_{timestamp}"

    # ✅ Step 3 – Generate the Allure HTML report
    subprocess.run([
        "allure.cmd", "generate", allure_results_dir,
        "-o", report_dir, "--clean"
    ], shell=True)

    # ✅ Step 4 – Open the report in browser
    subprocess.run(["allure.cmd", "open", report_dir], shell=True)
