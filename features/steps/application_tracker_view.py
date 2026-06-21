from behave import when, then
from pages.more_view import ApplicationTrackerPage



@when("the user opens the first system log entry")
def step_when_user_opens_log(context):
    context.app_tracker = ApplicationTrackerPage(context.page)
    context.app_tracker.click_first_log_entry()

@then("the user closes the system log popup")
def step_then_user_closes_log(context):
    context.app_tracker.close_system_logs()