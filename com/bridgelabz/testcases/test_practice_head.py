import pytest

from com.bridgelabz.pageObjects.PracticeHead.PracticeHead import PHPage
from com.bridgelabz.testcases.conftest import take_screenshot

@pytest.mark.usefixtures("login")
class TestPracticeHead:
    @pytest.mark.sanity
    def test_create_practice_head(self, login):
        try:
            ph = PHPage(login)
            ph.create_ph("Surriyaa sanity-1", "surriyaatestsanity5@gmail.com", 6374400088, "P&A Phase 2")
        except Exception as e:
            take_screenshot(login, "test_create_ph")
            raise e

    @pytest.mark.sanity
    def test_edit_practice_head(self, login):
        try:
            ph = PHPage(login)
            ph.edit_ph_contact("9918005551")
        except Exception as e:
            take_screenshot(login, "test_edit_ph")
            raise e