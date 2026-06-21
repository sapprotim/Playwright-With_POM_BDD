from playwright.sync_api import Page, Locator, expect
import time, random


class DoctorSendPostProgrammeSurvey:
    def __init__(self, page: Page):
        self.page = page
        self.checkbox_number: int = 0
        self.survey_sent_box: Locator | None = None

    def doctor_send_pps(self) -> bool:
        count = self.page.locator("//tbody/tr/td[5]//input[contains(@id, 'mat-mdc-checkbox')]").count()
        if count == 0:
            return False

        self.checkbox_number = random.randint(2, count)
        checkbox = self.page.locator(f"(//tbody/tr/td[5]//input[contains(@id, 'mat-mdc-checkbox')])[{self.checkbox_number}]")
        if not checkbox.is_enabled():
            return False
        checkbox.check()

        self.page.get_by_role("button", name="Send Post Programme Survey").click()
        time.sleep(1)
        self.page.get_by_role("button", name="Confirm").click()
        dismiss_btn = self.page.locator("#custom-alerts-to-users-success-message").get_by_text("Dismiss", exact=True)
        expect(dismiss_btn).to_be_visible()
        dismiss_btn.click()
        return True

    def get_survey_sent_box_locator(self) -> Locator:
        self.survey_sent_box = self.page.locator(f"(//tbody/tr)[{self.checkbox_number}]//td[6]/mat-chip-list/mat-chip/span[@class='survey-date']")
        return self.survey_sent_box