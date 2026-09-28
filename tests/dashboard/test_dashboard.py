import pytest
import allure
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity
from tools.allure.suites import AllureSuite
from tools.allure.suites import AllureParentSuite
from tools.allure.suites import AllureSubSuite
from tools.routes import AppRoute
from config import settings
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.suite(AllureSuite.DASHBOARD)
@allure.sub_suite(AllureSubSuite.DASHBOARD)
@allure.parent_suite(AllureParentSuite.LMS)
@pytest.mark.dashboard
@pytest.mark.regression
@allure.title("Check displaying of dashboard page")
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.severity(Severity.NORMAL)
def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit(AppRoute.DASHBOARD)
    dashboard_page_with_state.navbar.check_visible(settings.test_user.username)
    dashboard_page_with_state.sidebar.check_visible()
    dashboard_page_with_state.dashboard.check_visible_dashboard_title()
    dashboard_page_with_state.check_scores()
    dashboard_page_with_state.check_students()
    dashboard_page_with_state.check_activities()
    dashboard_page_with_state.check_courses()
