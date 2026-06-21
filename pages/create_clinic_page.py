import re
import time

from playwright.sync_api import Page, expect
from faker import Faker
fake = Faker()

class Create_clinica:
    def __init__(self, page: Page):
        self.page = page
    def add_clinic(self):
        name = "AT" + fake.name()
        address = "AT" + fake.address()
        self.page.get_by_role("button", name="+ Add New Clinic").click()
        self.page.get_by_role("textbox", name="Clinic Name").fill(name)
        self.page.get_by_role("textbox", name="Clinic Address").fill(address)
        self.page.locator("span", has_text="Parent Facility").click()
        self.page.locator("//div[@class='dropdown open']//ul[@class='dropdown-menu']/li[1]").click()
        self.page.get_by_text("Add Clinic").click()
        create_cliic = self.page.locator("//div[normalize-space()='Clinic added successfully']")
        self.page.locator("//div[@class='success-popup-msg ng-star-inserted']//button[@class='btn btn-primary ack-dismiss-btn'][normalize-space()='Dismiss']").click()
        return create_cliic

