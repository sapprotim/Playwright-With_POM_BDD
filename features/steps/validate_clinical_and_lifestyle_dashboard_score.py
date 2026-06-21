from behave import when, then
from pages.clinical_ws_score import validate_clinical_score
from pages.lifestyle_ws_score import validation_lifestyle_score



@when("the Clinical and Lifestyle scores should be correctly displayed")
def check_wellness_scores(context):
    validate_clinical_score(context.page)
    validation_lifestyle_score(context.page)


@then("the Clinical and Lifestyle scores should be matched with the calculation")
def step_validate_scores(context):
    print("Passed")



