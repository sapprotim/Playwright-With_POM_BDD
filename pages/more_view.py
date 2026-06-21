class ApplicationTrackerPage:
    def __init__(self, page):
        self.page = page

    def click_first_log_entry(self):
        self.page.locator("//body[1]/app-root[1]/div[3]/app-application-tracker[1]/div[2]/div[1]/div[1]/app-stm-logs[1]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[6]/a[1]").click()

    def close_system_logs(self):
        self.page.locator("//div[@id='system-logs']//img[@alt='Close button']").click()
