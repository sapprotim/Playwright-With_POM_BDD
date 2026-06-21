from behave import when, then
from pages.edit_user import EditWorkflowPage
import time

@when("the doctor selects and edits a user")
def step_impl(context):
    context.edit_user_page = EditWorkflowPage(context.page)
    context.edit_user_page.edit_myuser()

@then("the user data should be updated and confirmed")
def step_impl(context):
    result = context.edit_user_page.edit_user_functions()
    assert "Users profile updated successfully" in result.inner_text(), "Confirmation message not found"
    time.sleep(2)