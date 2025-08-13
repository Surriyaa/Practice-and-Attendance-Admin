import pytest
import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from com.bridgelabz.pageObjects.LoginLogout.SignInPage import SignInPage
from com.bridgelabz.utilities.read_config import ReadConfig
from com.bridgelabz.utilities.logger import Logger


@pytest.fixture(scope="session")
def chrome_browser(request):
    # Always pull TC_ID from test node if present
    tc_id = getattr(request.node, "tc_id", "TC_01")
    logger = Logger.get_logger("ChromeBrowserFixture", tc_id)

    logger.info("Initializing Chrome WebDriver with suppressed logs.")
    options = Options()
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(), options=options)

    logger.info("Maximizing browser window.")
    driver.maximize_window()

    logger.info("Setting implicit wait to 10 seconds.")
    driver.implicitly_wait(10)

    url = ReadConfig.get_url()
    logger.info(f"Navigating to URL: {url}")
    driver.get(url)

    yield driver

    logger.info("Quitting Chrome WebDriver.")
    driver.quit()


@pytest.fixture(scope="session")
def login(chrome_browser, request):
    tc_id = getattr(request.node, "tc_id", "TC_01")
    logger = Logger.get_logger("LoginFixture", tc_id)

    driver = chrome_browser
    logger.info("Instantiating SignInPage object.")
    signin = SignInPage(driver)

    logger.info("Waiting for and clicking 'Sign in with Google' button.")
    signin.handle_wait(driver)

    logger.info("Waiting for Google login popup to appear.")
    WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) > 1)

    logger.info("Switching to Google login popup window.")
    driver.switch_to.window(driver.window_handles[1])

    logger.info("Entering Google account email.")
    signin.enter_email(ReadConfig.get_email())
    logger.info("Clicking 'Next' after entering email.")
    signin.click_Next()

    logger.info("Entering Google account password.")
    signin.enter_password(ReadConfig.get_password())
    logger.info("Clicking 'Next' after entering password.")
    signin.click_Next()

    logger.info("Waiting for application window to become available.")
    WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) > 0)

    logger.info("Switching back to original application window.")
    driver.switch_to.window(driver.window_handles[0])

    logger.info("Attempting to close overlay popup after login, if present.")
    try:
        wait = WebDriverWait(driver, 15)
        overlay = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class,'fixed') and contains(@class,'z-50')]")
        ))
        driver.execute_script("arguments[0].style.display='none';", overlay)
        logger.info("Overlay popup closed after login.")
    except Exception:
        logger.info("No overlay popup found after login, proceeding.")

    return driver


def take_screenshot(driver, scenario_name, tc_id="TC_01"):
    logger = Logger.get_logger("Screenshot", tc_id)
    logger.info("Preparing to take screenshot.")

    screenshot_dir = "/Practice-Attendance-Admin/ScreenShots"
    logger.info(f"Ensuring screenshot directory exists at {screenshot_dir}.")
    os.makedirs(screenshot_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    screenshot_name = f"{scenario_name}_{timestamp}.png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_name)

    logger.info(f"Saving screenshot to {screenshot_path}.")
    driver.save_screenshot(screenshot_path)
    logger.info(f"Screenshot saved at {screenshot_path}")


@pytest.fixture(scope="function", autouse=True)
def redirect_to_home_after_each_test(chrome_browser, request):
    yield
    logger = Logger.get_logger("Screenshot", "TC_01")
    tc_id = getattr(request.node, "tc_id", "TC_01")
    try:
        home_url = "https://bl-practice-attendance-app-stg-187791816934.asia-south1.run.app/admin/add-admin"
        chrome_browser.get(home_url)
        logger.info(f"Redirecting back to home page: {home_url}")

    except Exception as e:
        logger.warning(f"Failed to redirect to home page: {e}")
