import pytest
from com.bridgelabz.pageObjects.COELabs.COELabs import COELabs
from com.bridgelabz.testcases.conftest import take_screenshot

@pytest.mark.usefixtures("login")
class TestCOE:
    # Test Data
    COE_NAME = "Automation COE-2"
    COE_DETAILS = "Automation Testing-2"
    LATITUDE = "19.12"
    LONGITUDE = "72.89"
    DISTANCE = "50"
    EDITED_DETAILS = "SRM TN Updated Automation"

    @pytest.mark.coe
    def test_create_coe(self, login):
        driver = login
        coe = COELabs(driver)

        try:
            coe.click_create_coe_button()
            coe.fill_create_coe_form(self.COE_NAME, self.COE_DETAILS, self.LATITUDE, self.LONGITUDE, self.DISTANCE)
            coe.click_create_button()

            assert self.COE_NAME in driver.page_source, "COE creation failed"
            print(f"COE Creation successful: '{self.COE_NAME}' found in page source")
        except Exception as e:
            take_screenshot(driver, "test_create_coe")
            raise e

    @pytest.mark.coe
    def test_edit_coe(self, login):
        driver = login
        coe = COELabs(driver)

        try:
            coe.click_edit_SRMTN_button()
            coe.edit_details(self.EDITED_DETAILS)
            coe.click_edit_button()

            assert self.EDITED_DETAILS in driver.page_source, "COE edit failed"
            print(f"COE Edit successful: '{self.EDITED_DETAILS}' found in page source")
        except Exception as e:
            take_screenshot(driver, "test_edit_coe")
            raise e
