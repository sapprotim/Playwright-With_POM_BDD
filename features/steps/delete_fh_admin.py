from behave import when, then
from pages.Delete import Delete

@when("the user deletes a Fullerton Health Admin")
def step_delete_fh_admin(context):
    context.delete_fh_admin = Delete(context.page)
    context.delete_success_msg = context.delete_fh_admin.fh_admin_delete()

@then("a successful deletion message should be shown")
def step_verify_deletion(context):
    assert "Fullerton Health Admin deleted successfully" in context.delete_success_msg