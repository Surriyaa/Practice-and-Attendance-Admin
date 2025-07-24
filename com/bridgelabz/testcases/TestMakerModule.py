from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.bridgelabz.pageObjects.MakerModule.MakerModule import MakerModule
from com.bridgelabz.testcases.conftest import take_screenshot

@pytest.mark.usefixtures("login")
class TestMakerModule:

    def test_create_maker_module(self, login):
        driver = login
        maker = MakerModule(driver)
        sleep(5)
        maker.click_maker_module()
        maker.click_create_module()

        # Select Module by value
        maker.select_module_dropdown(value=1)

        maker.fill_module_form(
            topic="Loops and Conditions",
            notes="https://notes.link",
            level1="https://level1.link",
            level2="https://level2.link",
            level3="https://level3.link"
        )

        maker.click_submit()
        sleep(2)

        try:
            toast_xpath = "//*[contains(text(),'added successfully')]"
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            print("Maker Module Created Successfully.")
        except Exception as e:
            take_screenshot(driver, "test_create_maker_module")
            raise AssertionError(f"Maker Module creation failed. Reason: {str(e)}")

    def test_edit_maker_module(self, login):
        driver = login
        maker = MakerModule(driver)
        sleep(5)
        maker.click_maker_module()
        maker.click_edit_module()

        try:
            topic_field = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, maker.topic_input_xpath))
            )
            topic_field.clear()
            topic_field.send_keys("Updated Topic")

            maker.click_submit()
            sleep(2)

            toast_xpath = "//*[contains(text(),'updated successfully')]"
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            print("Maker Module Edited Successfully.")
        except Exception as e:
            take_screenshot(driver, "test_edit_maker_module")
            raise AssertionError(f"Maker Module editing failed. Reason: {str(e)}")
