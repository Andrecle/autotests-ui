import pytest
import allure
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
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
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.suite(AllureSuite.COURSES)
@allure.sub_suite(AllureSubSuite.COURSES)
@allure.parent_suite(AllureParentSuite.LMS)
@pytest.mark.courses
@pytest.mark.regression
@allure.title("Create course")
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.severity(Severity.CRITICAL)
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit(AppRoute.CREATE_COURSE)

    create_course_page.create_course_toolbar_view.check_visible()
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
    create_course_page.create_course_form.check_visible(
        title="", max_score="0", min_score="0", description="", estimated_time=""
    )

    create_course_page.create_course_exercises_toolbar_view.check_visible()
    create_course_page.check_visible_exercises_empty_view()

    create_course_page.image_upload_widget.upload_preview_image("./testdata/files/image.png")
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
    create_course_page.create_course_form.fill(
        title="Playwright",
        max_score="100",
        min_score="10",
        description="Playwright",
        estimated_time="2 weeks"
    )
    create_course_page.create_course_toolbar_view.click_create_course_button()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
    )

@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.suite(AllureSuite.COURSES)
@allure.sub_suite(AllureSubSuite.COURSES)
@allure.parent_suite(AllureParentSuite.LMS)
@pytest.mark.courses
@pytest.mark.regression
@allure.title("Check displaying of empty courses list")
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.severity(Severity.NORMAL)
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit(AppRoute.COURSES)

    courses_list_page.navbar.check_visible(settings.test_user.username)
    courses_list_page.sidebar.check_visible()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()


@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.suite(AllureSuite.COURSES)
@allure.sub_suite(AllureSubSuite.COURSES)
@allure.parent_suite(AllureParentSuite.LMS)
@allure.title("Edit course")
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.severity(Severity.CRITICAL)
def test_edit_course(create_course_page: CreateCoursePage,courses_list_page: CoursesListPage):
    create_course_page.visit(AppRoute.CREATE_COURSE)
    create_course_page.image_upload_widget.upload_preview_image(settings.test_data.image_png_file)
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
    create_course_page.create_course_form.fill(
        title="Playwright",
        max_score="100",
        min_score="10",
        description="Playwright",
        estimated_time="2 weeks"
    )
    create_course_page.create_course_toolbar_view.click_create_course_button()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
    )
    courses_list_page.course_view.menu.click_edit(index=0)
    create_course_page.create_course_form.fill(
        title="New Playwright",
        estimated_time="3 weeks",
        description="New Playwright",
        max_score="1000",
        min_score="100"
    )
    create_course_page.create_course_toolbar_view.click_create_course_button()

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index=0, title="New Playwright", max_score="1000", min_score="100", estimated_time="3 weeks"
    )







