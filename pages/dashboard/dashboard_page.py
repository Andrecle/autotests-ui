from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarComponent
from components.charts.chart_view_component import ChartViewComponent

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard = DashboardToolbarComponent(page)
        self.charts_students = ChartViewComponent(page,"students","bar")
        self.charts_activities = ChartViewComponent(page,"activities","line")
        self.charts_courses = ChartViewComponent(page,"courses","pie")
        self.charts_scores = ChartViewComponent(page,"scores","scatter")

    def check_students(self):
        self.charts_students.check_visible("Students")

    def check_activities(self):
        self.charts_activities.check_visible("Activities")

    def check_courses(self):
        self.charts_courses.check_visible("Courses")

    def check_scores(self):
        self.charts_scores.check_visible("Scores")


