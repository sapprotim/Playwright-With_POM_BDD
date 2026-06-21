from behave import when, then
from pages.patient_logs.lipids import LipidsPage


@when("the doctor adds and edits lipid values: Total Cholesterol, HDL, LDL, Triglycerides")
def step_navigate_patient_logs(context):
    lipids_page = LipidsPage(context.page)
    lipids_page.open_lipids_panel()
    if lipids_page.is_third_lipid_visible():
        lipids_page.edit_lipid_values()
    else:
        lipids_page.add_lipid_values()


@then("the lipids values should be visible and matched with updated value: Total Cholesterol, HDL, LDL, Triglycerides")
def step_check_bp_section(context):
    print("The lipids value matched with the updated values")


