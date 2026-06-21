from behave import when, then
from pages.hpb_Menu import AdminPage
from global_state import global_state

@when('selects the "Prospects" user')
def step_impl(context):
    if global_state.navigate_to_prospects_user:
        return
    global_state.users_page = AdminPage(context.page)
    global_state.user_type_title = global_state.users_page.select_Prospects()
    global_state.navigate_to_prospects_user = True

@then('the "Prospects" user page is displayed')
def step_impl(context):
    assert global_state.user_type_title == "Prospects"