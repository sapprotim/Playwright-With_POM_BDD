import time
from importlib.metadata import pass_none


class Calendar:
    def __init__(self, page):
        self.page = page

    def calendar_filter_dropdown(self):
        self.page.locator("//input[@id='history-datepicker']").click()
        self.page.locator("//button[normalize-space()='Today']").click()
        self.page.locator("//input[@id='history-datepicker']").click()
        self.page.locator("//button[normalize-space()='Yesterday']").click()
        self.page.locator("//input[@id='history-datepicker']").click()
        self.page.locator("//button[normalize-space()='30 Days']").click()
        self.page.locator("//input[@id='history-datepicker']").click()
        self.page.locator("//button[normalize-space()='3 Months']").click()
        self.page.locator("//input[@id='history-datepicker']").click()
        self.page.locator("//button[normalize-space()='6 Months']").click()
        # self.page.locator("//input[@id='history-datepicker']").click()
        # self.page.locator("//button[normalize-space()='Custom range']").click()
        # self.page.locator("//td[@class='available active start-date']").click()
        # self.page.locator("//td[@class='available weekend active end-date']").click()


