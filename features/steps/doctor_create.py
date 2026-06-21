from behave import when, then
from pages.create.create_doctor import DoctorCreationPage
from global_state import global_state

@when("create a new Doctor")
def step_impl(context):
    if global_state.doctor_created:
        return

    context.doctor_page = DoctorCreationPage(context.page)
    context.success_message = context.doctor_page.create_doctor()
    global_state.doctor_created = True

@then("the Doctor should be created successfully")
def step_impl(context):
    assert "Doctor has been added successfully" in context.success_message