import re
import time

from playwright.sync_api import Page, expect
from faker import Faker

fake = Faker()


class CreateFH:
    def __init__(self, page: Page):
        self.page = page

    def add_fullerton_health(self):
        facility_name = "AT" + fake.company()
        facility_address = "AT" + fake.address()
        expect(self.page.get_by_role("button", name="+ Add New Fullerton Health")).to_be_visible()
        self.page.get_by_role("button", name="+ Add New Fullerton Health").click()
        self.page.get_by_role("textbox", name=re.compile("Fullerton Health Name")).fill(facility_name)
        self.page.get_by_role("textbox", name=re.compile("Fullerton Health Address")).fill(facility_address)
        self.page.get_by_text("Add Fullerton Health").click()
        success_message = self.page.locator("//div[normalize-space()='Fullerton Health added successfully']")
        expect(success_message).to_be_visible(timeout=5000)
        dismiss_btn = self.page.get_by_role("button", name="Dismiss")
        expect(dismiss_btn).to_be_visible()
        dismiss_btn.click()
        return success_message

