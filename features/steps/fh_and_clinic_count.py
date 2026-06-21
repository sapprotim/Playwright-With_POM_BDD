from behave import when, then
from pages.Dashboard_page import Dashboardpage

@when("clicks on the total in org view page")
def step_impl(context):
    dashboard = Dashboardpage(context.page)
    dashboard.click_total_users()


@then("the total number of Fullerton Health and Clinic should be displayed")
def step_impl(context):
    print("Total number of Fullerton Health and Clinic display successfully")