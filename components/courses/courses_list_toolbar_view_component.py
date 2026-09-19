import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button
from elements.icon import Icon

class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.title = Text(page,f'{identifier}-toolbar-title-text',"Title")
        self.create_course_button = Button(page,f'{identifier}-toolbar-create-course-button',"Create Button")
        self.icon = Icon(page,f'{identifier}-empty-view-icon',"Icon")

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text("Courses")
        self.create_course_button.check_visible()

    def click_create_course_button(self, current_url):
        self.create_course_button.click()
        # Дополнительно проверим, что произошел редирект на правильную страницу
        if current_url == "courses":
            self.check_current_url(re.compile(".*/#/courses/create"))
        elif current_url == "create":
            self.check_current_url(re.compile(".*/#/courses"))
