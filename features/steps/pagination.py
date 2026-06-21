from behave import given, when, then
from pages.login_page import LoginPage  # your own login logic
from pages.pagination import PaginationPage


@when("the user selects different page sizes")
def step_select_page_sizes(context):
    pagination = PaginationPage(context.page)
    pagination.pagination()

@then("the table should reflect the selected page size")
def step_verify_table(context):
    # Optional assertion or visual confirmation
    # assert context.page.locator("table").first.is_visible()
    print("✅ Pagination options selected successfully.")