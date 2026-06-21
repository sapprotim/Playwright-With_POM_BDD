from playwright.sync_api import Page, expect

class UserTableSort:
    def __init__(self, page: Page):
        self.page = page

    def sort_user_table(self):
        cells = ["NAME", "CLINIC"]
        for name in cells:
            locator = self.page.get_by_role("cell", name=name)
            if locator.count() > 0:  # check if it exists
                sort_button = locator.locator("img")
                sort_button.click()