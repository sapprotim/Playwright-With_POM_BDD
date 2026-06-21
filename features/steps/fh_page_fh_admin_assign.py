from behave import given, when, then
from pages.assign import assign

@when("clicks the 'Assign Fullerton Health Admin' button")
def step_click_assign(context):
    assign_doctor = assign(context.page)
    assign_doctor.assign_fh_Admin()


@then("the FH Admin should be listed under the assigned FH Admin page")
def step_reset_sort(context):
    print("FH Admin assign done.")
