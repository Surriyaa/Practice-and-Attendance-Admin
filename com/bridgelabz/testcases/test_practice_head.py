import pytest

from com.bridgelabz.pageObjects.PracticeHead.PracticeHead import PHPage
from com.bridgelabz.testcases.conftest import take_screenshot

@pytest.mark.usefixtures("login")
class TestPracticeHead:
    @pytest.mark.sanity
    def test_create_ph(self, login):
        try:
            ph = PHPage(login)
            ph.create_ph("Surriyaa sanity2", "surriyaatestsanity2@gmail.com", 6374400001, "P&A Phase 2")
        except Exception as e:
            take_screenshot(login, "test_create_ph")
            raise e

    @pytest.mark.sanity
    def test_edit_ph(self, login):
        try:
            ph = PHPage(login)
            ph.edit_ph_contact("9918001191")
        except Exception as e:
            take_screenshot(login, "test_edit_ph")
            raise e