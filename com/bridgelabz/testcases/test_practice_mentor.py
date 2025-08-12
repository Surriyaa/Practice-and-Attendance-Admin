import time
import random
from datetime import datetime

import pytest
import allure

from com.bridgelabz.pageObjects.PracticeMentor.PracticeMentorPage import MentorPage
from com.bridgelabz.testcases.conftest import take_screenshot

@allure.epic("Practice & Attendance Admin")
@allure.feature("Practice Mentor Module")
@allure.story("Validate Practice Mentor functionality")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login")
class TestPracticeMentor:

    @allure.title("TestPracticeMentor::test_create_mentor")
    @allure.story("Practice Mentor Creation Functionality")
    @pytest.mark.sanity
    def test_create_mentor(self, login, request):
        """
        Verify the Practice Mentor is created successfully.
        """
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id

        allure.dynamic.testcase(f"PracticeMentorCreate-{tc_id}")

        try:
            mentor = MentorPage(login, tc_id=tc_id)
            name = f"RandomMentor{int(time.time())}"
            email = f"randomemail{int(time.time())}@bridgelabz.com"
            mobile = f"{random.randint(6, 9)}{random.randint(100000000, 999999999)}"
            mentor.create_practice_mentor(name, email, mobile, "P&A Phase 2")
            allure.attach("Practice Mentor created successfully", name="Mentor Creation", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(login, "test_create_mentor", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"PracticeMentor creation failed due to: {e}")

    @allure.title("TestPracticeMentor::test_edit_mentor")
    @allure.story("Practice Mentor Edit Functionality")
    @pytest.mark.sanity
    def test_edit_mentor(self, login, request):
        """
        Verify the Practice Mentor contact is edited successfully.
        """
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id

        allure.dynamic.testcase(f"PracticeMentorEdit-{tc_id}")

        try:
            mentor = MentorPage(login, tc_id=tc_id)
            mobile = f"{random.randint(6, 9)}{random.randint(100000000, 999999999)}"
            mentor.edit_mentor_contact(mobile)
            allure.attach("Practice Mentor contact edited successfully", name="Mentor Edit", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(login, "test_edit_mentor", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"PracticeMentor edit failed due to: {e}")

    @allure.title("TestPracticeMentor::test_disable_mentor")
    @allure.story("Practice Mentor Disable Functionality")
    @pytest.mark.regular
    def test_disable_mentor(self, login, request):
        """
        Verify the Practice Mentor is disabled successfully.
        """
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id

        allure.dynamic.testcase(f"PracticeMentorDisable-{tc_id}")

        try:
            mentor = MentorPage(login, tc_id=tc_id)
            mentor.disable_mentor()
            allure.attach("Practice Mentor disabled successfully", name="Mentor Disable", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(login, "test_disable_mentor", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"PracticeMentor disable failed due to: {e}")