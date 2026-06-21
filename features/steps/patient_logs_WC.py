from behave import when, then
from pages.patient_logs.WC import WCPage
from pages.patient_logs.data_Validation import DataValidation


@when("the doctor adds and edits waist circumference")
def step_navigate_patient_logs(context):
    wc = WCPage(context.page)
    wc.WC_Add()
    wc.WC_edit()


@then("the waist circumference value should be visible and matched with updated value")
def step_check_bp_section(context):
    validator = DataValidation(context.page)
    validator.validate_waist_circumference()
    print("The waist circumference matched with the updated value")


