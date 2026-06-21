from behave import given, when, then
from pages.Edit_FH_admin import EditFH

@when("edits the information of FH admin")
def step_click_edit_user(context):
    edit_page = EditFH(context.page)
    edit_page.edit_fh()


@then("the updated details should appear in the FH admin's profile")
def step_update_user_details(context):
    print("Profile update done.")
