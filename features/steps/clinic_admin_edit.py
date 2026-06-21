from behave import when, then
from pages.Edit_Clinic_admin import EditClinic

@when("Edit the clinic admin details")
def step_edit_clinic_admin(context):
    context.edit_clinic_page = EditClinic(context.page)
    context.edit_success_message = context.edit_clinic_page.edit_clinic()

@then("Clinic admin should be updated successfully")
def step_verify_edit_clinic(context):
    assert "Clinic Admin updated successfully" in context.edit_success_message
