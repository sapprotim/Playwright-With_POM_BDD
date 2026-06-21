from playwright.sync_api import Page, expect

class RefreshablePage:
    def __init__(self, page: Page):
        self.page = page
        self.refresh_icon = page.locator("//img[@title='Refresh']")

    def refresh(self):
        rows = self.page.locator("//tbody/tr")
        count = rows.count()
        if count == 0:
            return 0
        else:
            expect(self.refresh_icon).to_be_visible(timeout=5000)
            expect(self.refresh_icon).to_be_enabled()
            self.refresh_icon.click()
            self.page.wait_for_timeout(1000)
            return 1