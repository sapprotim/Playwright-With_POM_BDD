from behave import when, then
from pages.Customer_Type import CustomerType
from global_state import global_state
from playwright.sync_api import expect

@when('the user selects all customer types one by one')
def step_impl(context):
    global_state.customer_type_page = CustomerType(context.page)
    global_state.customer_type_page.customtype()

@then('the last selected customer type should be Public')
def step_impl(context):
    last_selected = context.page.get_by_role("button", name="Public ▾")
    expect(last_selected).to_be_visible()