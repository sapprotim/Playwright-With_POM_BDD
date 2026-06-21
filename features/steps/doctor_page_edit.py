from behave import when, then
from pages.Edit_doctor_admin import Editdoctor
import time


@when("edits the information of doctor")
def step_impl(context):
    doctor = Editdoctor(context.page)
    context.update_message = doctor.edit_doctor()  # store returned text
    time.sleep(3)

@then("the updated details should appear in the doctor's profile")
def step_impl(context):
    assert context.update_message == "Doctor details updated successfully"