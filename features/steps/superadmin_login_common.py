from behave import given
from pages.login_page import LoginPage
from config.credentials import Org_Admin_password, Org_Admin_otp
import features.steps.global_state as global_state

@given("the super Admin is logged in")
def step_org_admin_login(context):
    print("Available context attributes:", dir(context))  # Debug line

    if global_state.login_done:
        return

    print("Trying to use:", context.superadminid)  # This will fail if not set

    login_page = LoginPage(context.page)
    login_page.navigate()
    login_page.login(context.superadminid, "SuperAdmin@123", Org_Admin_otp)

    global_state.login_done = True