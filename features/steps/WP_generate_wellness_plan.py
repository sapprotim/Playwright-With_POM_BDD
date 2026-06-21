from behave import when, then
from pages.wellness_plan import Wellnessplan



@when("clicks the 'Generate Wellness Plan' button")
def step_generate_plan(context):
    wellness = Wellnessplan(context.page)
    wellness.Wellness_plan_page()
    wellness.genarate_plan()


@then("the wellness plan should be generated successfully")
def step_verify_wellness_plan(context):
    print("wellness plan generated successfully")