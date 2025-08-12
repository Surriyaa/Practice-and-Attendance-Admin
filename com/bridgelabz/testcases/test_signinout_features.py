import pytest
from selenium.webdriver.common.by import By
from datetime import datetime

from com.bridgelabz.pageObjects.LoginLogout.SignInPage import SignInPage
from com.bridgelabz.testcases.conftest import take_screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.bridgelabz.utilities.testcasedecorator import test_case


@pytest.mark.usefixtures("login")
class TestSignIn:

    @pytest.mark.sanity
    def test_signin(self, login,request):
        # Generate TC_ID based on current seconds: "TC_<1–25>"
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id

        driver = login
        signin_page = SignInPage(driver, tc_id=tc_id)

        expected_title = "BL Practice App"

        try:
            WebDriverWait(driver, 10).until(EC.title_is(expected_title))
            print("Login successful. Title is:", driver.title)
        except:
            take_screenshot(driver, "test_signin", tc_id=tc_id)
            raise AssertionError(f"Title mismatch: Expected '{expected_title}', got '{driver.title}'")

    @pytest.mark.sanity
    def test_sign_out(self, login):
        # Generate TC_ID based on current seconds: "TC_<1–25>"
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        driver = login
        signin_page = SignInPage(driver, tc_id=tc_id)

        signin_page.click_logout()

        try:
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Welcome Back!")
            )
            print("Logout successful.")
        except:
            take_screenshot(driver, "test_sign_out", tc_id=tc_id)
            raise AssertionError("Logout failed: 'Welcome Back!' text not found on page.")