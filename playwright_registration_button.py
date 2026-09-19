from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    reg_button = page.get_by_test_id('registration-page-registration-button')
    expect(reg_button).to_be_disabled()

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    pass_input = page.get_by_test_id('registration-form-password-input').locator('input')
    pass_input.fill("password")

    expect(reg_button).to_be_enabled()
