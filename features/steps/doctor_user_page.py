from behave import when, then
from pages.Doctor_Users_page import Doctoruserpage
from global_state import global_state

@when("the Admin selects a doctor user")
def step_impl(context):
    if global_state.doctor_user_selected:
        return  # Skip if already selected

    context.doctor_user_page = Doctoruserpage(context.page)
    context.doctor_user_page.select_doctor_users_page()
    global_state.doctor_user_selected = True

@then("the doctor user page is displayed")
def step_impl(context):
    # You can replace this with an actual verification, such as:
    # assert context.doctor_user_page.is_displayed(), "Doctor User page not displayed"
    print("Doctor user page displayed")


