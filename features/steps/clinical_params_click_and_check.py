from behave import when, then
from pages.user_basic_info.wellness_score_tab import WellnessScoreTab
from global_state import global_state

@when("checks the clinical parameters")
def step_check_clinical_params(context):
    wellness = WellnessScoreTab(context.page)
    wellness.verify_clinical_value_format()


@then("the clinical parameters are shown")
def step_clinical_params_visible(context):
    wellness = WellnessScoreTab(context.page)
    wellness.verify_all_clinical_elements()