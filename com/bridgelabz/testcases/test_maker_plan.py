from time import sleep
import pytest
from com.bridgelabz.testcases.conftest import take_screenshot
from com.bridgelabz.pageObjects.MakerPlan.MakerPlanPage import MakerPlanPage



class TestMakerPlan:
    @pytest.mark.sanity
    def test_create_maker_plan(self, login):
        try:
            maker = MakerPlanPage(login)
            sleep(5)
            maker.create_maker_plan("Full Stack Testing 4", "58", description="This is An Automated Description 01")
        except Exception as e:
            take_screenshot(login, "test_create_maker_plan")
            raise e

    @pytest.mark.sanity
    def test_edit_maker_plan(self, login):
        try:
            maker = MakerPlanPage(login)
            maker.edit_module_in_plan("P & A Phase 2", "20")
        except Exception as e:
            take_screenshot(login, "test_edit_maker_plan")
            raise e