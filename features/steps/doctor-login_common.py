import time

from behave import given
from pages.login_page import LoginPage
from config.credentials import Stm_Admin_email, Stm_Admin_password, Stm_Admin_otp
from features.steps.global_state import login_done  # import the global flag
import features.steps.global_state as global_state  # import module to modify variable

@given("the doctor Admin is logged in")
def step_org_admin_login(context):
    if global_state.login_done:
        return  # Already logged in, skip

    login_page = LoginPage(context.page)
    login_page.navigate()
    login_page.login(Stm_Admin_email, Stm_Admin_password, Stm_Admin_otp)
    time.sleep(2)
    close_btn = context.page.locator("//img[@class='close-button']")
    if close_btn.is_visible():
        close_btn.click()
    global_state.login_done = True
