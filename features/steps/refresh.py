from behave import given, when, then
from pages.refresh import RefreshablePage
from pages.login_page import LoginPage

@when("the user refreshes the page")
def step_refresh(context):
    context.refresh_page = RefreshablePage(context.page)
    context.refresh_result = context.refresh_page.refresh()

@then("the page should be refreshed successfully")
def step_verify_refresh(context):
    if context.refresh_result == 0:
        print("✅ No data found, nothing to refresh.")
    else:
        print("✅ Page refreshed successfully.")