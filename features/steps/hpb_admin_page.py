from behave import when, then
from pages.hpb_Menu import AdminPage
from global_state import global_state

@when("selects the HPB Admin role")
def step_impl(context):
    if global_state.hpb_admin_selected:
        return  # Skip if already selected

    context.admin_page = AdminPage(context.page)
    context.actual_title = context.admin_page.select_HPB_admin()
    global_state.hpb_admin_selected = True

@then("the HPB Admin user list should be displayed")
def step_impl(context):
    assert context.actual_title == "HPB Admin", f"Expected title to be 'HPB Admin', but got '{context.actual_title}'"