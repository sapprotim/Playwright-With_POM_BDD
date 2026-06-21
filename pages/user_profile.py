import time
import random
import re
from playwright.sync_api import Page, expect


class UserProfileSearch:
    def __init__(self, page: Page):
        self.page = page
        self.random_name = None

    def search_user_profile(self):
        time.sleep(5)
        rows = self.page.locator("//tbody/tr")
        count = rows.count()
        if count == 0:
            return None
        i = random.randint(1, count)
        full_text = self.page.locator(f"//tbody/tr[{i}]/td[1]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        self.random_name = name_only

        self.page.fill("input[placeholder='Search']", name_only)

        # Wait for the search results to update
        first_result = self.page.locator("//tbody/tr[1]/td[1]/div[1]/div[1]/div[1]/span[1]")
        expect(first_result).to_be_visible(timeout=5000)
        first_result.click()