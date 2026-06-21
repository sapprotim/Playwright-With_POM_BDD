from behave import when, then
from pages.Delete import Delete

@when("the user deletes a clinic Admin")
def step_delete_clinic_admin(context):
    # Create page object and store in Behave context
    context.delete_page = Delete(context.page)
    # Store the returned success message string
    context.delete_success_msg = context.delete_page.clinic_admin_delete()

@then("Clinic Admin successful deletion message should be shown")
def step_verify_deletion(context):
    assert "Clinic Admin deleted successfully" in context.delete_success_msg