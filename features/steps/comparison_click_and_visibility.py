from behave import given, when, then
from pages.user_basic_info.trends_comparison import UserComparisonPage

@when("clicks on the comparison section")
def step_click_comparison(context):
    comparison_section = UserComparisonPage(context.page)
    comparison_section.verify_clinical_comparison_selection()
    comparison_section.verify_lifestyle_comparison_selection()

@then("the comparison section becomes visible")
def step_verify_comparison_visible(context):
    comparison_section = UserComparisonPage(context.page)
    comparison_section.verify_dashboard_sections_visibility()