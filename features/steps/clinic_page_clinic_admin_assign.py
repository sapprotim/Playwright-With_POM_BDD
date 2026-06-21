from behave import given, when, then
from pages.assign import assign

@when("clicks the 'Assign Clinic Admin' button")
def step_click_assign(context):
    assign_doctor = assign(context.page)
    assign_doctor.assign_Clinic_Admin()


@then("the Clinic Admin should be listed under the assigned Clinic Admin page")
def step_reset_sort(context):
    print("Clinic Admin assign done.")
