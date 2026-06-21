from behave import when, then
from pages.hpb_Menu import AdminPage
from global_state import global_state

@when("the user selects the Invited Users tab")
def step_select_invited_users(context):
    if global_state.invite_user_selected:
        return  # Skip if already selected

    context.base_page = AdminPage(context.page)
    context.base_page.select_invite_user()
    global_state.invite_user_selected = True

@then("the Invited Users tab should be displayed")
def step_invited_users_tab_displayed(context):
    element = context.page.locator("//div[@class='user-list-title']")
    assert element.is_visible(), "The 'user-list-title' element is not visible"

