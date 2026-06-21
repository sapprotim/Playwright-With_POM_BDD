from behave import given
from pages.login_page import LoginPage
from config.credentials import clinic_email, clinic_password, clinic_otp
import features.steps.global_state as global_state

@given("the Clinic Admin is logged in")
def step_org_admin_login(context):
    if global_state.login_done:
        return  # Already logged in, skip

    login_page = LoginPage(context.page)
    login_page.navigate()
    login_page.login(clinic_email, clinic_password, clinic_otp)

    global_state.login_done = True  # set flag to True after login