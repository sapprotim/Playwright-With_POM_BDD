from behave import when, then
from pages.hpb_Menu import AdminPage
from global_state import global_state

@when("the user selects the Programme Completed Users tab")
def step_select_programme_completed_users(context):
    if global_state.select_programme_completed_user:
        return  # Skip if already selected

    context.base_page = AdminPage(context.page)
    context.base_page.select_programme_completed_user()
    global_state.select_programme_completed_user = True

@then("the Programme Completed Users tab should be displayed")
def step_programme_completed_users_tab_displayed(context):
    programme_completed = context.page.locator("//div[@class='user-list-title']")
    assert programme_completed.is_visible()