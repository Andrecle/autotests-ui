import pytest
import allure
from allure_commons.types import Severity
from tools.routes import AppRoute
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.suites import AllureSuite
from tools.allure.suites import AllureParentSuite
from tools.allure.suites import AllureSubSuite
from config import settings
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.suite(AllureSuite.AUTHENTICATION)
@allure.sub_suite(AllureSubSuite.REGISTRATION)
@allure.parent_suite(AllureParentSuite.LMS)
@allure.severity(Severity.CRITICAL)
def test_successful_registration(dashboard_page: DashboardPage, registration_page: RegistrationPage):
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.fill_registration_form(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password
    )
    registration_page.click_registration_button()

    dashboard_page.dashboard.check_visible_dashboard_title()









