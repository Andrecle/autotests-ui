from playwright.sync_api import Page
import allure
from components.base_component import BaseComponent
from elements.text import Text

class DashboardToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_title = Text(page,'dashboard-toolbar-title-text',"Title")

    @allure.step('Check visible dashboard title')
    def check_visible_dashboard_title(self):
        self.dashboard_title.check_visible()
        self.dashboard_title.check_have_text("Dashboard")