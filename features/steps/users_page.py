from behave import when,then
from pages.hpb_Menu import AdminPage
from global_state import global_state

@when('the Admin opens the Users page')
def step_impl(context):
    if global_state.navigate_to_users_tab:
        return
    global_state.users_page = AdminPage(context.page)
    global_state.users_page.select_user()
    global_state.navigate_to_users_tab = True

@then('the Users page should be displayed')
def step_impl(context):
    # For example: verify if title or any known element exists
    assert context.page.locator("//div[@class='user-list-title']").is_visible()