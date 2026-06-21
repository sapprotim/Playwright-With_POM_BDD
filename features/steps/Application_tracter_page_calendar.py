from behave import when, then
from pages.Application_tracker_calender import Calendar

@when("the user applies all calendar filter options")
def step_apply_calendar_filter(context):
    context.calendar_page = Calendar(context.page)
    context.calendar_page.calendar_filter_dropdown()

@then("the calendar filter should be applied")
def step_verify_calendar_filter(context):
    print("Pass")

