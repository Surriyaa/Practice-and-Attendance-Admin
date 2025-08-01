import pytest
from com.bridgelabz.pageObjects.PracticeHead.PracticeHead import PHPage
from com.bridgelabz.testcases.conftest import take_screenshot
from com.bridgelabz.utilities.data_loader import read_practice_head_data
from com.bridgelabz.utilities.logger import Logger

@pytest.mark.usefixtures("login")
class TestPracticeHead:
    @pytest.mark.sanity
    def test_create_practice_head(self, login):
        logger = Logger.get_logger(self.__class__.__name__)
        try:
            logger.info("----- Starting Test: test_create_practice_head -----")
            ph = PHPage(login)
            ph.click_ph_tab()
            ph.click_add_ph_button()
            ph.enter_name("Surriyaa sanity-1")
            ph.enter_email("surriyaatestsanity5@gmail.com")
            ph.enter_mobile("6374400088")
            ph.select_base_coe("P&A Phase 2")
            ph.click_create_button()
            ph.verify_email("surriyaatestsanity5@gmail.com")
            logger.info("----- Test Passed: test_create_practice_head -----")
        except Exception as e:
            logger.error("Exception occurred in test_create_practice_head", exc_info=True)
            take_screenshot(login, "test_create_ph")
            raise e

    @pytest.mark.sanity
    def test_edit_practice_head(self, login):
        logger = Logger.get_logger(self.__class__.__name__)
        try:
            logger.info("----- Starting Test: test_edit_practice_head -----")
            ph = PHPage(login)
            ph.click_ph_tab()
            ph.click_edit_icon()
            ph.enter_new_mobile("9918005551")
            ph.click_update_button()
            logger.info("----- Test Passed: test_edit_practice_head -----")
        except Exception as e:
            logger.error("Exception occurred in test_edit_practice_head", exc_info=True)
            take_screenshot(login, "test_edit_ph")
            raise e

    # Load test data from Excel
    excel_file_path = "C:/Users/ASUS/PycharmProjects/Practice-Attendance-Admin/com/bridgelabz/test_data/practice_head_details.xlsx"
    test_data = read_practice_head_data(excel_file_path, "Sheet1")

    @pytest.mark.parametrize("name,email,mobile,base_coe,expected_result", test_data)
    def test_create_practice_head_data_driven(self, login, name, email, mobile, base_coe, expected_result):
        ph = PHPage(login)
        try:
            ph.click_ph_tab()
            ph.click_add_ph_button()
            ph.enter_name(name)
            ph.enter_email(email)
            ph.enter_mobile(mobile)
            ph.select_base_coe(base_coe)   #antha submmit button work agalanalu fail pannanu da
            ph.click_create_button()

            if expected_result.lower() == "pass":
                ph.verify_email(email)
            else:
                pytest.fail(f"Expected failure but test passed for: {email}")

        except Exception as e:
            if expected_result.lower() == "fail":
                # Test expected to fail, so pass it
                assert True
            else:
                take_screenshot(login, f"ph_creation_failed_{email}")
                raise e