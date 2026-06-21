from behave import when, then
from pages.Delete import Delete

@when("the user deletes a Doctor Admin")
def step_delete_doctor_admin(context):
    context.delete_page = Delete(context.page)  # ✅ don't overwrite context
    context.delete_success_msg = context.delete_page.doctor_admin_delete()

@then("Doctor Admin successful deletion message should be shown")
def step_verify_deletion(context):
    assert "Doctor deleted successfully" in context.delete_success_msg