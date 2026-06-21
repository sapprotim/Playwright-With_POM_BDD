from behave import given, when, then
from pages.assign import assign

@when("clicks the 'Assign Doctor' button")
def step_click_assign(context):
    assign_doctor = assign(context.page)
    assign_doctor.assign_doctor()

@then("the doctor should be listed under the assigned clinic")
def step_reset_sort(context):
    print("Doctor assigned done.")
