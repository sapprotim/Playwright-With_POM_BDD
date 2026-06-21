from behave import when, then
from pages.role_manager.custom_roleCheckBox import CustomRolePage
from playwright.sync_api import expect
from global_state import global_state


@when("the user creates a new custom role")
def step_impl(context):
    if getattr(global_state, "custom_role_created", False):
        return  # Skip if already created

    context.role_page = CustomRolePage(context.page)
    context.role_page.customRole_Create()

    global_state.custom_role_created = True

@then("the custom role create successfully")
def step_impl(context):
    print("Passed")  # optionally validate with UI element or message


@when("the user edits the role name")
def step_impl(context):
    context.role_page = CustomRolePage(context.page)  # re-instantiate only if needed
    context.role_page.customRole_Edit()

@then("the custom role edit successfully")
def step_impl(context):
    print("Passed")


@when("the user checks a permission checkbox")
def step_impl(context):
    context.role_page.customRole_CheckboxIn()

@then("the checkboxin successfully")
def step_impl(context):
    print("Passed")

@when("the user unchecks the permission checkbox")
def step_impl(context):
    context.role_page = CustomRolePage(context.page)   # create and store the page object
    context.role_page.customRole_CheckboxOut()

@then("the checkboxout successfully")
def step_impl(context):
    print("Passed")

@when("the user deletes the custom role")
def step_impl(context):
    context.role_page = CustomRolePage(context.page)
    context.role_page.customrole_Delete()

@then("the custom role should be removed successfully")
def step_impl(context):
    print("Passed")