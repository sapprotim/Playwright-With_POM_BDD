import random
import time

from playwright.sync_api import Page, expect
from faker import Faker
from .phone_number import generate_fake_sg_phone


class EditFH:
    def __init__(self, page: Page):
        self.page = page
        self.fake = Faker()
    def edit_fh(self):
        self.page.locator("//img[@src='./assets/images/edit.png']").first.click()
        self.page.get_by_role("textbox", name="First Name").click()
        self.page.get_by_role("textbox", name="Last Name").click()
        self.page.get_by_role("textbox", name="Email ID").click()
        self.page.get_by_role("button", name="Clear all").click()

        self.page.locator("ng-select").filter(has_text="Country").locator("span").first.click()
        country = "Singapore"
        self.page.fill("//input[@placeholder='search country']", country)
        self.page.get_by_role("option", name=country).click()

        self.page.locator("//div[@class='selected-dial-code']").click()
        self.page.get_by_role("textbox", name="Search Country").fill("Singapore")
        self.page.locator("//span[@class='iti__country-name'][normalize-space()='Singapore']").click()

        self.page.fill("//input[@id='phone']", generate_fake_sg_phone())
        self.page.get_by_text("Next").first.click()

        self.page.get_by_text("Assign Additional Roles").click()
        self.page.locator("hpb-add-on-roles").get_by_text("Save Changes").click()

        self.page.wait_for_selector("//div[normalize-space()='Fullerton Health Admin updated successfully']")
        text = self.page.locator(
            "//div[normalize-space()='Fullerton Health Admin updated successfully']").inner_text()
        self.page.get_by_role("button", name="Dismiss").click()
        return text

