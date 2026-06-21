class IframeBoardPage:
    def __init__(self, page):
        self.page = page

    def access_public_board(self):
        self.page.get_by_role("img", name="Copy Passcode").click()

    def access_public_board_mobile(self):
        self.page.locator("//div[@class='navigation-bar-option active']").click()