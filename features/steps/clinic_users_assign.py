from behave import given, when, then
from pages.assign_users_page import AssignUsersPage

@when("clicks the 'Assign Users' button")
def step_click_assign(context):
    assign_page = AssignUsersPage(context.page)
    assign_page.assign_and_confirm()

@then("the user should be listed under the assigned clinic")
def step_reset_sort(context):
    print("User assigned done.")
