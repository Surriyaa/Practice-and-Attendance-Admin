import os
import shutil
from datetime import datetime

def generate_allure_report():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    results_dir = "reports/allure_results_1"
    report_dir = f"reports/allure_html_{timestamp}"

    os.system(f"allure generate {results_dir} -o {report_dir} --clean")
    print(f"✅ Allure report generated at: {report_dir}")

if __name__ == "__main__":
    generate_allure_report()
