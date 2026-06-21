from behave import given
from pages.login_page import LoginPage
from config.credentials import Org_Admin_email, Org_Admin_password, Org_Admin_otp
import features.steps.global_state as global_state

@given("the HPB Admin is logged in")
def step_org_admin_login(context):
    if global_state.login_done:
        return  # Already logged in, skip

    login_page = LoginPage(context.page)
    login_page.navigate()
    login_page.login(Org_Admin_email, Org_Admin_password, Org_Admin_otp)

    global_state.login_done = True  # set flag to True after login



