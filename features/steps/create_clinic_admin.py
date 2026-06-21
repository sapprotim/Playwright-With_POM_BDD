from behave import when, then
from pages.create.Create_Clinica import create_clinic_page
from global_state import global_state

@when("Add a new Clinic Admin user")
def add_new_clinic_admin(context):
    if global_state.clinic_admin_created:
        return  # Skip if already added
    context.create_clinic_admin_page = create_clinic_page(context.page)
    context.successfully_text = context.create_clinic_admin_page.create_clinic_admin()
    global_state.clinic_admin_created = True

@then("the Clinic Admin should be created successfully")
def verify_clinic_admin_creation(context):
    assert "Clinic Admin added successfully." in context.successfully_text