import time
from playwright.sync_api import Page
from config.credentials import url


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = url

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username, password, otp):
        self.page.fill("input[name='username']", username)
        self.page.fill("input[name='password']", password)
        self.page.click("input[value='Sign In']")
        time.sleep(2)
        self.page.wait_for_selector("input[id='inp']")
        self.page.fill("input[id='inp']", str(otp))
        self.page.click("input[value='Submit']")


