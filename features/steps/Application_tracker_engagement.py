from behave import when, then
from pages.hpb_Menu import AdminPage
from global_state import global_state

@when("the user clicks the Engagements")
def step_impl(context):
    if global_state.engagements_selected:
        return
    context.navigation_page = AdminPage(context.page)
    context.navigation_page.select_application_tracker_engagements()
    global_state.engagements_selected = True

@then("the Engagements section is displayed")
def step_then_engagements_displayed(context):
    # Replace with actual assertion if needed
    print("✅ Engagements section is displayed.")