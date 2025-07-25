import pytest
import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.bridgelabz.pageObjects.LoginLogout.SignInPage import SignInPage
from com.bridgelabz.utilities.read_config import ReadConfig


@pytest.fixture(scope="function")
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(ReadConfig.get_url())
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(chrome_browser):
    driver = chrome_browser
    signin = SignInPage(driver)

    # Wait and click the "Sign in with Google" button
    signin.handle_wait(driver)

    # Switch to Google login popup window
    WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[1])

    # Wait and perform Google login steps
    signin.enter_email(ReadConfig.get_email())
    signin.click_Next()

    signin.enter_password(ReadConfig.get_password())
    signin.click_Next()

    # Switch back to original application window
    WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) > 0)
    driver.switch_to.window(driver.window_handles[0])

    # === CLOSE OVERLAY POPUP IMMEDIATELY AFTER LOGIN ===
    try:
        wait = WebDriverWait(driver, 15)
        overlay = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class,'fixed') and contains(@class,'z-50')]")
        ))
        driver.execute_script("arguments[0].style.display='none';", overlay)
        print("Overlay popup closed after login.")
    except:
        print("No overlay popup found after login, proceeding.")

    return driver


def take_screenshot(driver, scenario_name):
    screenshot_dir = "ScreenShots/"
    os.makedirs(screenshot_dir, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    screenshot_name = f"{scenario_name}_{timestamp}.png"
    screenshot_path = os.path.join(screenshot_dir, screenshot_name)

    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at {screenshot_path}")
