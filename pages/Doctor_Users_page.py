import time
from playwright.sync_api import Page, expect


class Doctoruserpage:
    def __init__(self, page: Page):
        self.page = page

    def select_doctor_users_page(self):
        doctor_user_link = self.page.locator("//tbody/tr[1]/td[1]/a[1]")
        doctor_user_link.click()
        time.sleep(7)

    def select_clinic_users_page(self):
        self.page.locator("//tbody/tr[1]/td[1]/img[1]").click()
        self.page.locator("//tbody/tr[2]/td[1]/span").click()