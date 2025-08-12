import random
import time
from datetime import datetime

import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.bridgelabz.pageObjects.Admin.Admin import AdminPage
from com.bridgelabz.testcases.conftest import take_screenshot
from com.bridgelabz.utilities.logger import Logger


@allure.epic("Practice & Attendance Admin")
@allure.feature("Admin Management Module")
@allure.story("Validate Admin Management functionality")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.sanity
@pytest.mark.usefixtures("login")
class TestAdminFunctionality:

    @allure.title("TestAdminFunctionality::test_create_admin_valid")
    @allure.story("Create Admin with Valid Details")
    def test_create_admin_valid(self, request, login):
        """
        Verify that a new admin can be created successfully with valid details.
        """
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id

        allure.dynamic.testcase(f"AdminValidCreate-{tc_id}")

        try:
            page = AdminPage(login, tc_id=tc_id)
            page.navigate_to_admin_tab()
            page.click_add_admin()
            email = f"randomemail{int(time.time())}@bridgelabz.com"
            mobile = f"{random.randint(6, 9)}{random.randint(100000000, 999999999)}"
            page.enter_admin_details("Super Admin", email, mobile)
            page.click_create()
            toast_xpath = "//*[contains(text(),'successfully')]"

            WebDriverWait(login, 15).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            allure.attach("Admin created successfully", name="Admin Creation", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(login, "test_create_admin_valid", tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("Admin creation failed: " + str(e))

    @allure.title("TestAdminFunctionality::test_create_admin_duplicate_email")
    @allure.story("Duplicate Email Admin Creation")
    def test_create_admin_duplicate_email(self, request, login):
        """
        Verify that creating an admin with a duplicate email shows proper error.
        """
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id

        allure.dynamic.testcase(f"AdminDuplicateEmail-{tc_id}")

        try:
            page = AdminPage(login, tc_id=tc_id)
            page.navigate_to_admin_tab()
            page.click_add_admin()
            page.enter_admin_details("Super Admin", "surriyaapps@gmail.com", "6374161480")
            page.click_create()
            page.click_cancel()
            toast_xpath = "//*[contains(text(),'already registered')]"

            WebDriverWait(login, 15).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            allure.attach("Duplicate email error verified", name="Duplicate Email", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(login, "test_create_admin_duplicate_email", tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("Duplicate email error not shown: " + str(e))

    @allure.title("TestAdminFunctionality::test_edit_admin")
    @allure.story("Edit Admin Details")
    def test_edit_admin(self, request, login):
        """
        Verify that admin details can be edited successfully.
        """
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id

        allure.dynamic.testcase(f"AdminEdit-{tc_id}")

        try:
            page = AdminPage(login, tc_id=tc_id)
            page.navigate_to_admin_tab()
            page.click_edit_admin()
            mobile = f"{random.randint(6, 9)}{random.randint(100000000, 999999999)}"
            page.edit_admin_contact_details(mobile)
            page.click_update()
            toast_xpath = "//*[contains(text(),'successfully')]"

            WebDriverWait(login, 15).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            allure.attach("Admin edited successfully", name="Admin Edit", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(login, "test_edit_admin", tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail("Admin edit failed: " + str(e))