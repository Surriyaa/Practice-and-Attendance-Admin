import pytest

from com.bridgelabz.pageObjects.PracticeMentor.PracticeMentorPage import MentorPage
from com.bridgelabz.testcases.conftest import take_screenshot

@pytest.mark.usefixtures("login")
class TestPracticeMentor:
    @pytest.mark.sanity
    def test_create_mentor(self, login):
        try:
            mentor = MentorPage(login)
            mentor.create_practice_mentor("Surriyaa sanity5", "surriysanity5@bridgelabz.com", "6354670109",
                                          "P&A Phase 2")
        except Exception as e:
            take_screenshot(login, "test_create_mentor")
            raise e

    @pytest.mark.sanity
    def test_edit_mentor(self, login):
        try:
            mentor = MentorPage(login)
            mentor.edit_mentor_contact("9876555521")
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