from behave import given, when, then
from pages.Edit_Clinic_admin import EditClinic

@when("edits the information of clinic admin")
def step_click_edit_user(context):
    edit_page = EditClinic(context.page)
    edit_page.edit_clinic()


@then("the updated details should appear in the clinic admin's profile")
def step_update_user_details(context):
    print("Profile update done.")
