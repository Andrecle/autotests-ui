import pytest
import allure

from config import settings
from tools.routes import AppRoute
from tools.allure.tags import AllureTag
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity
from tools.allure.suites import AllureSuite
from tools.allure.suites import AllureParentSuite
from tools.allure.suites import AllureSubSuite

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),
        ("  ", "password")
    ]
)
@pytest.mark.xdist_group(name="authorization-group")
@allure.title("User login with wrong email or password")
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.suite(AllureSuite.AUTHENTICATION)
@allure.sub_suite(AllureSubSuite.AUTHORIZATION)
@allure.parent_suite(AllureParentSuite.LMS)
@allure.severity(Severity.CRITICAL)
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit(AppRoute.LOGIN)
    login_page.login_form.fill_login_form(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()

@pytest.mark.xdist_group(name="authorization-group")
@allure.title("Registration with correct email, username and password")
@allure.tag(AllureTag.REGRESSION,AllureTag.AUTHORIZATION,AllureTag.USER_LOGIN)
@pytest.mark.regression
@pytest.mark.authorization
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.suite(AllureSuite.AUTHENTICATION)
@allure.sub_suite(AllureSubSuite.AUTHORIZATION)
@allure.parent_suite(AllureParentSuite.LMS)
@allure.severity(Severity.BLOCKER)
def test_successful_authorization(
        login_page: LoginPage,
        dashboard_page: DashboardPage,
        registration_page: RegistrationPage
):
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.fill_registration_form(email=settings.test_user.email, username=settings.test_user.username, password=settings.test_user.password)
    registration_page.click_registration_button()

    dashboard_page.dashboard.check_visible_dashboard_title()
    dashboard_page.navbar.check_visible(settings.test_user.username)
    dashboard_page.sidebar.check_visible()
    dashboard_page.sidebar.click_logout()

    login_page.login_form.fill_login_form(email=settings.test_user.email, password=settings.test_user.password)
    login_page.click_login_button()

    # Проверка элементов Dashboard после входа
    dashboard_page.dashboard.check_visible_dashboard_title()
    dashboard_page.navbar.check_visible(settings.test_user.username)
    dashboard_page.sidebar.check_visible()
@allure.tag(AllureTag.REGRESSION,AllureTag.AUTHORIZATION,AllureTag.NAVIGATION)
@allure.title("Navigation from login page to registration page")
@pytest.mark.regression
@pytest.mark.authorization
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.suite(AllureSuite.AUTHENTICATION)
@allure.sub_suite(AllureSubSuite.AUTHORIZATION)
@allure.parent_suite(AllureParentSuite.LMS)
@allure.severity(Severity.NORMAL)
def test_navigate_from_authorization_to_registration(
        login_page: LoginPage,
        registration_page: RegistrationPage
):
    login_page.visit(AppRoute.LOGIN)
    login_page.click_registration_link()

    registration_page.registration_form.check_visible(email="", username="", password="")