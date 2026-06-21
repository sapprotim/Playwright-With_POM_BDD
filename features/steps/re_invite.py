from behave import when, then
from pages.re_invite import re_invite

@when("resends the invite")
def step_impl(context):
    invite = re_invite(context.page)
    context.reinvite_message = invite.re_invite()

@then("the Re_Invitation has been resent successfully")
def step_impl(context):
    assert context.reinvite_message == "Invitation resent successfully"
