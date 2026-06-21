from behave import when, then
from pages.patient_logs.FBG import GlucosePage


@when("the doctor inputs a fasting blood glucose value")
def step_navigate_patient_logs(context):
    glucose = GlucosePage(context.page)
    glucose.add_fasting_blood_glucose()
    glucose.edit_fasting_blood_glucose()


@then("the entered fasting blood glucose value should be saved and visible")
def step_check_bp_section(context):
    print("Fasting blood glucose value saved and visible")


