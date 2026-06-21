from behave import when, then
from pages.user_basic_info.wellness_score_tab import WellnessScoreTab
from global_state import global_state

@when("the admin clicks View filter and Calendar")
def step_check_clinical_params(context):
    wellness = WellnessScoreTab(context.page)
    wellness.view_filter_buttons()


@then("the filter and Calendar buttons should be visible")
def step_clinical_params_visible(context):
    wellness = WellnessScoreTab(context.page)
    wellness.calendar_parameter_images()