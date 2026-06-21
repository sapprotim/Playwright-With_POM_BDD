from behave import when, then
from pages.patient_logs.BP import BloodPressurePage
from pages.patient_logs.data_Validation import DataValidation


@when("the blood pressure section should be able to input data")
def step_navigate_patient_logs(context):
    bp = BloodPressurePage(context.page)
    bp.add_blood_pressure()


@then("blood pressure readings should be listed and matches with the inputted data")
def step_check_bp_section(context):
    validator = DataValidation(context.page)
    validator.validate_blood_pressure()


