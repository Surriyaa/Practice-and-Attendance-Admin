import pytest
import allure
from time import sleep
import time
from datetime import datetime
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.bridgelabz.pageObjects.MakerModule.MakerModule import MakerModule
from com.bridgelabz.testcases.conftest import take_screenshot
from com.bridgelabz.utilities.data_loader import load_questions_from_excel

@allure.epic("Practice & Attendance Admin")
@allure.feature("Maker Module")
@allure.story("Validate Maker Module functionality")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("login")
class TestMakerModule:

    @allure.title("TestMakerModule::test_create_maker_module")
    @allure.story("Maker Module Creation Functionality")
    @pytest.mark.sanity
    def test_create_maker_module(self, login, request):
        """
        Verify the Maker Module is created successfully.
        """
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id
        allure.dynamic.testcase(f"MakerModuleCreate-{tc_id}")

        driver = login
        maker = MakerModule(driver, tc_id=tc_id)
        sleep(5)
        maker.click_maker_module()
        maker.click_create_module()

        maker.select_module_dropdown(value=1)
        topic = f"randomtopic{int(time.time())}"
        maker.fill_module_form(
            topic=topic,
            notes="https://www.w3schools.com/java/java_while_loop.asp",
            level1="https://www.w3schools.com/java/java_while_loop_do.asp",
            level2="https://www.w3schools.com/java/java_for_loop.asp",
            level3="https://www.w3schools.com/java/java_while_loop_reallife.asp"
        )

        maker.click_submit()
        sleep(2)

        try:
            toast_xpath = "//*[contains(text(),'added successfully')]"
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            allure.attach("Maker Module Created Successfully.", name="Success", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            take_screenshot(driver, "test_create_maker_module", tc_id=tc_id)
            allure.attach(str(e), name="Error", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"Maker Module creation failed. Reason: {str(e)}")

    @allure.title("TestMakerModule::test_edit_maker_module")
    @allure.story("Maker Module Edit Functionality")
    @pytest.mark.sanity
    def test_edit_maker_module(self, login, request):
        """
        Verify the Maker Module is edited successfully.
        """
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        request.node.tc_id = tc_id
        allure.dynamic.testcase(f"MakerModuleEdit-{tc_id}")

        driver = login
        maker = MakerModule(driver, tc_id=tc_id)
        sleep(5)
        maker.click_maker_module()
        maker.click_edit_module()

        try:
            topic_field = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, maker.topic_input_xpath))
            )
            actions = ActionChains(driver)
            actions.click(topic_field)
            actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
            topic = f"Updated Random Topic {int(time.time())}"
            topic_field.send_keys(topic)

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

    @pytest.mark.regular
    def test_disable_maker_module(self, login):
        # Generate TC_ID based on current seconds: "TC_<1–25>"
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        driver = login
        maker = MakerModule(driver, tc_id=tc_id)
        sleep(5)
        maker.click_maker_module()
        maker.click_disable_button()

        try:
            toast_xpath = "//*[contains(text(),'disabled successfully')]"
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, toast_xpath))
            )
            print("Maker Module disabled Successfully.")
        except Exception as e:
            take_screenshot(driver, "test_disable_maker_module")
            raise AssertionError(f"Maker Module disabling failed. Reason: {str(e)}")

    # Load Excel questions
    excel_path = "C:/Users/ASUS/PycharmProjects/Practice-Attendance-Admin/com/bridgelabz/test_data/questions.xlsx"
    question_data = load_questions_from_excel(excel_path)

    @pytest.mark.parametrize("question", question_data["level1"])
    def test_add_level1_questions(self, login, question):
        # Generate TC_ID based on current seconds: "TC_<1–25>"
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        page = MakerModule(login, tc_id=tc_id)
        page.add_level1_question(question)

    @pytest.mark.parametrize("question", question_data["level2"])
    def test_add_level2_questions(self, login, question):
        # Generate TC_ID based on current seconds: "TC_<1–25>"
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        page = MakerModule(login, tc_id=tc_id)
        page.add_level2_question(question)

    @pytest.mark.parametrize("question", question_data["level3"])
    def test_add_level3_questions(self, login, question):
        # Generate TC_ID based on current seconds: "TC_<1–25>"
        tc_number = (datetime.now().second % 25) + 1
        tc_id = f"TC_{tc_number}"
        page = MakerModule(login, tc_id=tc_id)
        page.add_level3_question(question)