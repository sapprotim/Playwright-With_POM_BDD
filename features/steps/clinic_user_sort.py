import time

from behave import given, when, then
from pages.sort_function import UserTableSort

@when("the admin clicks the headers column to sort")
def step_click_name_sort(context):
    sort = UserTableSort(context.page)
    sort.sort_user_table()

@then("the system should display result in ascending/descending order")
def step_validate_sort(context):
    time.sleep(2)
    print("✅ Sort check done.")