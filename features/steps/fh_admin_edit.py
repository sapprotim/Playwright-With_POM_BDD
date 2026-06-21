from behave import when, then
from pages.Edit_FH_admin import EditFH

@when("the user edits a Fullerton Health Admin user")
def step_edit_fh_admin(context):
    context.edit_fh = EditFH(context.page)
    context.result_text = context.edit_fh.edit_fh()

@then("the changes should be saved successfully")
def step_verify_edit(context):
    assert context.result_text == "Fullerton Health Admin updated successfully"
