from behave import when, then
from pages.create.Create_FH_Admin import CreateFullertonHealthPage
from global_state import global_state

@when("Add a new Fullerton Health Admin user")
def add_new_fh_admin(context):
    if global_state.fh_admin_created:
        return  # Skip if already added

    context.create_fh_admin_page = CreateFullertonHealthPage(context.page)
    context.successfully_text = context.create_fh_admin_page.create_fh_admin()

    global_state.fh_admin_created = True

@then("the Fullerton Health Admin should be created successfully")
def verify_creation(context):
    assert "Fullerton Health Admin has been added successfully" in context.successfully_text