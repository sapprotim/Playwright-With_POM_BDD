from asyncio import timeout

from playwright.sync_api import Page, expect
import time

class AdminPage:
    def __init__(self, page: Page):
        self.page = page

    def open_admin_tab(self):
        self.page.locator(".tab-name").first.click()

    def open_Organization_View(self):
        # self.open_admin_tab()
        # time.sleep(2)
        # self.page.get_by_text("Organization View").click()
        self.page.get_by_text("Clinic").first.click()
        self.page.get_by_text("Organization View").click()
        time.sleep(3)
        self.page.mouse.move(960, 540)

    def select_HPB_admin(self):
        self.open_admin_tab()
        hpb_admin = self.page.get_by_text("HPB Admin", exact=True).first
        expect(hpb_admin).to_be_visible()
        hpb_admin.click()
        title = self.page.locator("//div[@class='user-list-title']")
        expect(title).to_be_visible()
        self.page.mouse.move(960, 540)
        return title.inner_text().strip()

    def select_fullerton_admin(self):
        self.open_admin_tab()
        fullerton_admin = self.page.get_by_text("Fullerton Health Admin", exact=True).first
        expect(fullerton_admin).to_be_visible()
        fullerton_admin.click()
        time.sleep(3)
        title = self.page.locator("//div[@class='user-list-title']")
        text = title.inner_text().strip()
        self.page.mouse.move(960, 540)
        return text

    def select_clinic(self):
        self.open_admin_tab()
        self.page.get_by_text("Clinic Admin", exact=True).first.click()
        title = self.page.locator("//div[@class='user-list-title']")
        self.page.mouse.move(960, 540)
        return title.inner_text().strip()

    def select_doctor_admin(self):
        self.open_admin_tab()
        self.page.get_by_text("Doctor", exact=True).click()
        time.sleep(1)
        self.page.mouse.move(960, 540)
        return True

    def select_Prospects(self):
        time.sleep(1)
        self.open_admin_tab()
        self.page.locator("a").filter(has_text="Users").click()
        time.sleep(1)
        users_Prospects = self.page.locator("//a[@routerlink='/user-prospects']")
        expect(users_Prospects).to_be_visible()
        users_Prospects.click()
        self.page.mouse.move(960, 540)
        time.sleep(2)
        title = self.page.locator("//div[normalize-space()='Prospects']")
        return title.inner_text().strip()



    def select_user(self):
        time.sleep(1)
        self.open_admin_tab()
        self.page.locator("a").filter(has_text="Users").click()
        users = self.page.locator("//a[@routerlink='/users']")
        expect(users).to_be_visible()
        users.click()
        self.page.mouse.move(960, 540)
        time.sleep(5)
        # self.page.locator("//img[@title='Refresh']").click()

    def select_zendesk_user(self):
        time.sleep(1)
        self.open_admin_tab()
        time.sleep(1)
        self.page.locator("//a[normalize-space()='Users']").click()
        time.sleep(1)
        self.page.locator("//a[@routerlink='/zendesk-users']").click()
        time.sleep(5)
        self.page.mouse.move(960, 540)


    def select_invite_user(self):
        time.sleep(1)
        self.page.locator("//div[@class='user-list-title']//div[@class='dropdown']/button").click()
        invite_user = self.page.get_by_text("Invited Users")
        expect(invite_user).to_be_visible()
        invite_user.click()
        time.sleep(5)
        self.page.mouse.move(960, 540)

    def select_withdrawn_user(self):
        time.sleep(1)
        self.page.locator("//div[@class='user-list-title']//div[@class='dropdown']/button").click()
        withdrawn_user = self.page.get_by_text("Withdrawn Users")
        expect(withdrawn_user).to_be_visible()
        withdrawn_user.click()
        time.sleep(5)
        self.page.mouse.move(960, 540)


    def select_programme_completed_user(self):
        time.sleep(1)
        self.page.locator("//div[@class='user-list-title']//div[@class='dropdown']/button").click()
        programme_completed = self.page.get_by_text("Programme Completed Users")
        expect(programme_completed).to_be_visible()
        programme_completed.click()
        time.sleep(5)
        self.page.mouse.move(960, 540)

    def select_All_user(self):
        try:
            time.sleep(5)
            self.page.locator("//div[@class='user-list-title']/div//button").click()
        except:
            try:
                self.page.locator("//div[@class='user-list-title']//div[@class='dropdown']//button").click()
            except:
                pass  # Optional: you can log or raise error if both are not found
        # Then click the common "All Users" link
        self.page.locator("//div[@class='user-list-title']//li[1]").click()
        time.sleep(5)
        self.page.mouse.move(960, 540)

    def select_user_metrics(self):
        time.sleep(1)
        self.open_admin_tab()
        time.sleep(1)
        self.page.locator("//a[normalize-space()='Users']").click()
        time.sleep(1)
        self.page.locator("//a[normalize-space()='User Metrics']").first.click()
        time.sleep(5)
        title = self.page.locator("//h1[normalize-space()='User Metrics']")
        self.page.mouse.move(960, 540)
        return title

    def select_user_to_Doctor(self):
        time.sleep(1)
        self.page.locator("//button[normalize-space()='Users']").click()
        self.page.locator("//div[@class='dropdown open']/ul/li[2]/a").click()
        self.page.mouse.move(960, 540)
        time.sleep(5)

    def select_doctor_to_Clinic_Admin(self):
        time.sleep(1)
        self.page.locator("//button[normalize-space()='Doctor']").click()
        self.page.locator("//a[@id='FacilityAdministrator']").click()
        self.page.mouse.move(960, 540)
        time.sleep(5)

    def select_Structure_page(self):
        self.page.locator("//div[@id='admin']").click()
        self.page.get_by_text("Structure").click()
        self.page.mouse.move(960, 540)
        time.sleep(5)

    def select_fh_user(self):
        self.page.locator("//tbody/tr/td[1]/span").first.click()
        self.page.mouse.move(960, 540)
        time.sleep(5)

    def select_application_tracker(self):
        self.page.locator("//span[normalize-space()='Application Tracker']").click()
        self.page.mouse.move(960, 540)
        time.sleep(5)

    def select_application_tracker_engagements(self):
        self.page.get_by_role("link", name="Engagements").click()
        self.page.mouse.move(960, 540)
        time.sleep(4)



