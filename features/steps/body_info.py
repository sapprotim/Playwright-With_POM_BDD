from behave import given, when, then
from pages.user_basic_info.user_BasicInfo import UserBasicInfoPage
from pages.user_profile import UserProfileSearch

@when("the user checks the body info")
def step_impl(context):
    context.body_info = UserBasicInfoPage(context.page)
    context.body_info.verify_body_info()

@then("the user body info is shown")
def step_body_info_shown(context):
    print("User body info is displayed")

