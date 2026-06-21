from behave import when, then
from pages.hpb_Menu import AdminPage
from global_state import global_state

@when("the user selects the Withdrawn Users tab")
def step_select_withdrawn_users(context):
    if global_state.withdrawn_user_selected:
        return  # Skip if already selected

    context.base_page = AdminPage(context.page)
    context.base_page.select_withdrawn_user()
    global_state.withdrawn_user_selected = True

@then("the Withdrawn Users tab should be displayed")
def step_withdrawn_users_tab_displayed(context):
    withdrawn_user = context.page.locator("//div[@class='user-list-title']")
    assert withdrawn_user.is_visible()