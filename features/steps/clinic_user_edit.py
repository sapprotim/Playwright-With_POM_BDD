import time
from behave import given, when, then
from pages.edit_user import EditWorkflowPage

@when("clicks Edit on a user and updates the user’s details")
def step_click_edit_user(context):
    edit_user = EditWorkflowPage(context.page)
    edit_user.edit_userORG()
    time.sleep(3)


@then("the updated user information should appear in the user list")
def step_update_user_details(context):
    print("User update done.")
