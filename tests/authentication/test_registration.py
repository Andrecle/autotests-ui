import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(dashboard_page: DashboardPage, registration_page: RegistrationPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.registration_form.fill_registration_form(
        email="user.name@gmail.com",
        username="username",
        password="password"
    )
    registration_page.click_registration_button()

    dashboard_page.dashboard.check_visible_dashboard_title()









