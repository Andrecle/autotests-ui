from playwright.sync_api import Page, expect
import re
import allure
from tools.logger import get_logger

logger = get_logger("BASE PAGE")

class BasePage:
    def __init__(self, page: Page): 
        self.page = page

    def visit(self, url: str):  # Метод для открытия ссылок
        step = f'Opening the url "{url}"'
        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until='networkidle')

    def reload(self):  # Метод для перезагрузки страницы
        step = f'Reloading page with url "{self.page.url}"'
        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: re.Pattern[str]):
        step = f'Checking that current url matches pattern "{expected_url.pattern}"'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)