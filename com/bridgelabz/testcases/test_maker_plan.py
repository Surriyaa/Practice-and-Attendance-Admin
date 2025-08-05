from time import sleep
import pytest
from com.bridgelabz.testcases.conftest import take_screenshot
from com.bridgelabz.pageObjects.MakerPlan.MakerPlanPage import MakerPlanPage

@pytest.mark.usefixtures("login")
class TestMakerPlan:

    @pytest.mark.sanity
    def test_create_maker_plan(self, login):
        try:
            maker = MakerPlanPage(login)
            sleep(1)
            maker.click_maker_plan_tab()
            maker.click_add_maker_plan_button()
            maker.enter_maker_plan_name("Full Stack Testing 8")
            maker.enter_duration("58")
            maker.enter_description("This is An Automated Description 08")
            maker.click_submit_button()
        except Exception as e:
            take_screenshot(login, "test_create_maker_plan")
            raise e

    @pytest.mark.sanity
    def test_edit_maker_plan(self, login):
        try:
            maker = MakerPlanPage(login)
            sleep(1)
            maker.click_maker_plan_tab()
            maker.open_maker_plan_dropdown()
            maker.select_maker_plan("P & A Phase 2")
            maker.click_edit_icon()
            maker.edit_duration("210")
            maker.save_changes()
        except Exception as e:
            take_screenshot(login, "test_edit_maker_plan")
            raise e

    @pytest.mark.regular
    def test_disable_maker_plan(self, login):
        try:
            maker = MakerPlanPage(login)
            sleep(1)
            maker.click_maker_plan_tab()
            maker.open_maker_plan_dropdown()
            maker.select_maker_plan("Full Stack Testing 1")
            maker.click_disable_maker_module_button()
        except Exception as e:
            take_screenshot(login, "test_disable_maker_plan")
            raise e