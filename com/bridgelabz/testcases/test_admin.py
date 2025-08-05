# tests/test_admin_operations.py
import random
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.bridgelabz.pageObjects.Admin.Admin import AdminPage
from com.bridgelabz.testcases.conftest import take_screenshot


@pytest.mark.usefixtures("login")  # Fixture that provides driver
class TestAdminFunctionality:

    def test_create_admin_valid(self, login):
        driver = login
        page = AdminPage(driver)
        page.navigate_to_admin_tab()
        page.click_add_admin()
        email = f"randomemail{int(time.time())}@bridgelabz.com"
        mobile = f"{random.randint(6, 9)}{random.randint(100000000, 999999999)}"
        page.enter_admin_details("Super Admin", email, mobile)
        page.click_create()
        # Verify success toast
        toast_xpath = "//*[contains(text(),'successfully')]"

        try:
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            print("Toast message verified: File upload successfully.")
        except Exception as e:
            take_screenshot(driver, "test_create_admin_valid")
            raise AssertionError("Toast message not found or mismatch. " + str(e))

    def test_create_admin_duplicate_email(self, login):
        driver = login
        page = AdminPage(driver)
        page.navigate_to_admin_tab()
        page.click_add_admin()
        page.enter_admin_details("Super Admin", "surriyaapps@gmail.com", "6374161480")
        page.click_create()
        page.click_cancel()
        # Verify success toast
        toast_xpath = "//*[contains(text(),'already registered')]"

        try:
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            print("Toast message verified: File upload successfully.")
        except Exception as e:
            take_screenshot(driver, "test_create_admin_duplicate_email")
            raise AssertionError("Toast message not found or mismatch. " + str(e))

    def test_edit_admin(self, login):
        driver = login
        page = AdminPage(driver)
        page.navigate_to_admin_tab()
        page.click_edit_admin()
        mobile = f"{random.randint(6, 9)}{random.randint(100000000, 999999999)}"
        page.edit_admin_contact_details(mobile)
        page.click_update()
        # Verify success toast
        toast_xpath = "//*[contains(text(),'successfully')]"

        try:
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            print("Toast message verified: File upload successfully.")
        except Exception as e:
            take_screenshot(driver, "test_edit_admin")
            raise AssertionError("Toast message not found or mismatch. " + str(e))


