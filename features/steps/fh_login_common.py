import time
from behave import given
from pages.login_page import LoginPage
from config.credentials import fh_email, fh_password, fh_otp
from features.steps.global_state import login_done  # import the global flag
import features.steps.global_state as global_state  # import module to modify variable

@given("the fullerton health admin is logged in")
def step_org_admin_login(context):
    if global_state.login_done:
        return  # Already logged in, skip

    login_page = LoginPage(context.page)
    login_page.navigate()
    login_page.login(fh_email, fh_password, fh_otp)

    global_state.login_done = True  # set flag to True after login
    time.sleep(5)