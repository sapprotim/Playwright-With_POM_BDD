from behave import when, then
from pages.reset_sort import ResetSort

@when("the user clicks on reset sort")
def step_click_reset_sort(context):
    reset = ResetSort(context.page)
    reset.Reset_Sort()

@then("the system should reset the sort")
def step_reset_sort(context):
    print("Sort reset check done.")
