import random
import time

from playwright.sync_api import Page, expect
from faker import Faker
from .phone_number import generate_fake_sg_phone


class EditClinic:
    def __init__(self, page: Page):
        self.page = page
        self.fake = Faker()

    def edit_clinic(self):
        time.sleep(2)
        self.page.locator("//body[1]/app-root[1]/div[3]/app-view-department-list[1]/div[1]/div[3]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/div[1]/img[1]").first.click()
        time.sleep(2)
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

        # phone number
        self.page.fill("//input[@id='phone']", generate_fake_sg_phone())
        time.sleep(2)
        self.page.locator("//div[contains(text(),'Next')]").click()

        # self.page.locator(".schedule-drop-value > img").first.click()
        # list_items = self.page.locator("//div[@class='dropdown open']//ul[@class='dropdown-menu']//li")
        # count = list_items.count()
        # list_items.nth(random.randint(0, count - 1)).click()
        #
        # self.page.locator(".schedule-custom-dropdown > .dropdown > .schedule-drop-value > img").first.click()
        # list_items = self.page.locator("//div[@class='dropdown open']//ul[@class='dropdown-menu']/li")
        # count = list_items.count()
        # list_items.nth(random.randint(0, count - 1)).click()
        self.page.locator("app-assign-org-facility-dept").get_by_text("Save Changes").click()
        time.sleep(1)
        edit_message = self.page.locator("//div[normalize-space()='Clinic Admin updated successfully']").text_content()
        self.page.get_by_role("button", name="Dismiss").click()
        return edit_message
