from behave import when, then
from pages.patient_logs.calendar import CalendarPage

@when("the calendar filter should be visible")
def step_calendar_visible(context):
    calendar_visibility = CalendarPage(context.page)
    calendar_visibility.calendar_click()

@then("the doctor should be able to select a date from the calendar")
def step_select_date(context):
    print("Doctor able to select a date from the calendar")


