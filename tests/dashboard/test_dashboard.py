import pytest

from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_page_with_state.navbar.check_visible("username")
    dashboard_page_with_state.sidebar.check_visible()
    dashboard_page_with_state.dashboard.check_visible_dashboard_title()
    dashboard_page_with_state.check_scores()
    dashboard_page_with_state.check_students()
    dashboard_page_with_state.check_activities()
    dashboard_page_with_state.check_courses()
