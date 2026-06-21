from behave import given, when, then

@then("the user should land on the dashboard")
def step_verify_dashboard(context):
    context.page.wait_for_url("**/organization/structure-view", timeout=10000)
    assert "/organization/structure-view" in context.page.url
    context.login_done = True

@then("the user should land on the dashboard clinic")
def step_verify_dashboard(context):
    context.page.wait_for_url("**/#/users", timeout=10000)  # Use glob pattern
    assert "#/users" in context.page.url, f"Expected URL to include '#/users', but got {context.page.url}"
    context.login_done = True

@then("the fullerton health admin should land on the dashboard")
def step_verify_dashboard(context):
    context.page.wait_for_url("**/#/organization/structure-view", timeout=10000)  # Use glob pattern
    assert "#/organization/structure-view" in context.page.url, f"Expected URL to include '#/users', but got {context.page.url}"
    context.login_done = True

@then("the user should land on the dashboard doctor")
def step_verify_dashboard(context):
    context.page.wait_for_url("**/#/supportteam/*", timeout=10000)  # Glob match for any team ID
    assert "#/supportteam/" in context.page.url, f"Expected URL to include '#/supportteam/', but got {context.page.url}"
    context.login_done = True
