import time
from playwright.sync_api import Page
delete_fh_admin = "Auto "
delete_clinic_admin = "Playwright"
delete_doctor_admin = "Playwright"

class Delete:
    def __init__(self, page: Page):
        self.page = page
    def delete_cancel(self):
        self.page.get_by_role("button", name="Cancel").click()

    def delete_clinic(self):
        self.page.locator("//tbody/tr[1]/td[1]/img[1]").click()
        self.page.locator("//tr[2]//img[@src='./assets/images/delete.png']").click()
        self.page.locator("//button[normalize-space()='Delete Clinic']").click()
        self.page.locator("//button[@class='btn btn-primary ack-dismiss-btn'][normalize-space()='Dismiss']").click()


    def delete_FH(self):
        self.page.locator("//img[@src='./assets/images/delete.png']").first.click()
        self.page.locator("//div[@class='modal-content']//div[@class='modal-body']//div//button[@class='btn btn-primary delete-medi-btn'][normalize-space()='Delete Fullerton Health']").click()
        self.page.get_by_text("Dismiss").click()



    def fh_admin_delete(self):
        time.sleep(2)
        self.page.locator("//input[@placeholder='Search']").type(delete_fh_admin)
        time.sleep(1)
        self.page.wait_for_selector("//img[@src='./assets/images/delete.png']").click()
        self.page.locator("//button[normalize-space()='Delete Fullerton Health Admin']").click()
        time.sleep(1)
        self.page.wait_for_selector("//span[normalize-space()='Fullerton Health Admin deleted successfully']")
        successfully_text = self.page.locator("//span[normalize-space()='Fullerton Health Admin deleted successfully']")
        self.page.locator("//div[@id='success-message']//button[@class='btn btn-primary ack-dismiss-btn-custom'][normalize-space()='Dismiss']").click()
        return successfully_text.inner_text()

    def clinic_admin_delete(self):
        # Search for the clinic admin
        self.page.locator("//input[@placeholder='Search']").fill(delete_clinic_admin)
        # Wait for delete icon to appear and click
        self.page.wait_for_selector("//body[1]/app-root[1]/div[3]/app-department-admin-list[1]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/div[1]/img[2]")
        self.page.locator("//body[1]/app-root[1]/div[3]/app-department-admin-list[1]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/div[1]/img[2]").click()
        self.page.locator("//*[@id='delete-dept-admin']/div/div/div/div/app-delete-department-admin/div/div[3]//button[2]").click()
        self.page.wait_for_selector("//span[normalize-space()='Clinic Admin deleted successfully']")
        success_text = self.page.locator( "//span[normalize-space()='Clinic Admin deleted successfully']").inner_text()
        self.page.locator("//div[@id='success-message']//button[@class='btn btn-primary ack-dismiss-btn-custom'][normalize-space()='Dismiss']").click()
        return success_text

    def doctor_admin_delete(self):
        self.page.locator("//input[@placeholder='Search']").fill(delete_doctor_admin)
        time.sleep(2)
        self.page.wait_for_selector("//tbody/tr[1]/td[4]/div[1]/img[2]")
        self.page.locator("//tbody/tr[1]/td[4]/div[1]/img[2]").click()
        self.page.locator("//button[normalize-space()='Delete']").click()
        time.sleep(2)
        self.page.wait_for_selector("//span[normalize-space()='Doctor deleted successfully']")
        success_text = self.page.locator("//span[normalize-space()='Doctor deleted successfully']").text_content()
        self.page.locator("//div[@id='success-message']//button[@class='btn btn-primary ack-dismiss-btn-custom'][normalize-space()='Dismiss']").click()
        return success_text


