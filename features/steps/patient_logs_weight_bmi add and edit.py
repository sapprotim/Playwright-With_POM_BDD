from behave import when, then
from pages.patient_logs.weight_bmi import BodyShapePage
from pages.patient_logs.data_Validation import DataValidation


@when("the doctor adds and edits weight and BMI")
def step_navigate_patient_logs(context):
    weight_bmi = BodyShapePage(context.page)
    weight_bmi.add_weight_bmi()
    weight_bmi.edit_weight_bmi()


@then("the values of weight and BMI should be matched with the updated values")
def step_check_bp_section(context):
    validator = DataValidation(context.page)
    validator.validate_weight()
    validator.validate_bmi()
    print("The Weight and BMI matched with the updated values")


