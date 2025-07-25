import pytest
from selenium.webdriver.common.by import By

from com.bridgelabz.pageObjects.LoginLogout.SignInPage import SignInPage
from com.bridgelabz.testcases.conftest import take_screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("login")
class TestSignIn:

    @pytest.mark.sanity
    def test_signin(self, login):
        driver = login
        expected_title = "BL Practice App"

        try:
            WebDriverWait(driver, 10).until(EC.title_is(expected_title))
            print("Login successful. Title is:", driver.title)
        except:
            take_screenshot(driver, "test_signin")
            raise AssertionError(f"Title mismatch: Expected '{expected_title}', got '{driver.title}'")

    @pytest.mark.sanity
    def test_sign_out(self, login):
        driver = login
        signin_page = SignInPage(driver)

        signin_page.click_logout()

        try:
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Welcome Back!")
            )
            print("Logout successful.")
        except:
            take_screenshot(driver, "test_sign_out")
            raise AssertionError("Logout failed: 'Welcome Back!' text not found on page.")
