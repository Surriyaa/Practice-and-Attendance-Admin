import time
import random

import pytest

from com.bridgelabz.pageObjects.PracticeMentor.PracticeMentorPage import MentorPage
from com.bridgelabz.testcases.conftest import take_screenshot

@pytest.mark.usefixtures("login")
class TestPracticeMentor:
    @pytest.mark.sanity
    def test_create_mentor(self, login):
        try:
            mentor = MentorPage(login)
            name = f"RandomMentor{int(time.time())}"
            email = f"randomemail{int(time.time())}@bridgelabz.com"
            mobile = f"{random.randint(6, 9)}{random.randint(100000000, 999999999)}"
            mentor.create_practice_mentor(name, email, mobile, "P&A Phase 2")
        except Exception as e:
            take_screenshot(login, "test_create_mentor")
            raise e

    @pytest.mark.sanity
    def test_edit_mentor(self, login):
        try:
            mentor = MentorPage(login)
            mobile = f"{random.randint(6, 9)}{random.randint(100000000, 999999999)}"
            mentor.edit_mentor_contact(mobile)
        except Exception as e:
            take_screenshot(login, "test_edit_mentor")
            raise e

    @pytest.mark.regular
    def test_disable_mentor(self, login):
        try:
            mentor = MentorPage(login)
            mentor.disable_mentor()
        except Exception as e:
            take_screenshot(login, "test_disable_mentor")
            raise e