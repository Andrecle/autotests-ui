import pytest
from pages.courses.courses_list_page import CoursesListPage
from tools.routes import AppRoute
from config import settings

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit(AppRoute.COURSES)

    courses_list_page.navbar.check_visible(settings.test_user.username)
    courses_list_page.sidebar.check_visible()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()
    courses_list_page.toolbar_view.click_create_course_button("courses")
