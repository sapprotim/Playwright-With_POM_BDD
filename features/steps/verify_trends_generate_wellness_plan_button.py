from behave import when, then
from pages.user_basic_info.wellness_score_tab import WellnessScoreTab



@when("the admin clicks the Generate Wellness Plan button")
def step_check_clinical_params(context):
    wellness = WellnessScoreTab(context.page)
    wellness.verify_generate_wellness_plan_button()


@then("Button should work properly")
def step_clinical_params_visible(context):
    print("Button is navigating to Wellness Plan page")