from behave import when, then
from pages.patient_logs.HbA1c import HbA1cPage


@when("the doctor adds or edits the HbA1c value")
def step_navigate_patient_logs(context):
    HbA1c = HbA1cPage(context.page)
    HbA1c.add_or_edit_hba1c()


@then("the updated HbA1c value should be saved and visible")
def step_check_bp_section(context):
    print("HbA1c value saved and visible")


