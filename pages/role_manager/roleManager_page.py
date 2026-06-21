import time
import re
from playwright.sync_api import Page, expect

class RoleManagerPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_WP(self):
        role_manager_button = self.page.locator("//span[normalize-space()='Role Manager']")
        role_manager_button.click()
        time.sleep(2)