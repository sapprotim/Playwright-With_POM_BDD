from behave import given, when, then
from pages.user_basic_info.user_BasicInfo import UserBasicInfoPage
from pages.user_profile import UserProfileSearch

@when("the user checks the basic info")
def step_impl(context):
    context.user_info = UserBasicInfoPage(context.page)
    context.age = context.user_info.verify_basic_info()

@then("the user age is shown")
def step_impl(context):
    print("User age:", context.age)
    assert 25 <= context.age <= 75

