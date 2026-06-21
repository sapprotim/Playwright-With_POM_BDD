from behave import when, then
from pages.user_basic_info.wellness_score_tab import WellnessScoreTab
from global_state import global_state

@when("selects a start date and an end date")
def step_check_clinical_params(context):
    wellness = WellnessScoreTab(context.page)
    wellness.calendar_filter_dropdown()


@then("the system should display data within the selected date range")
def step_clinical_params_visible(context):
    print("selected date rang opened")