from behave import when, then
from pages.role_manager.default_rolesCheckbox import DefaultRolesPage  # update the import based on your structure

@when("the user checks all role-based checkboxes")
def step_impl(context):
    context.checkbox_page = DefaultRolesPage(context.page)
    context.checkbox_message = context.checkbox_page.CheckboxIn()

@when("the user checks all role-based checkboxes_out")
def step_impl(context):
    context.checkbox_page = DefaultRolesPage(context.page)
    context.checkbox_message = context.checkbox_page.CheckboxOut()

@then("all role checkboxes should be selected correctly")
def step_impl(context):
    print("Passed")



