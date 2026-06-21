from behave import given, when, then
from pages.user_basic_info.user_BasicInfo import UserBasicInfoPage
from pages.user_profile import UserProfileSearch

@when("the user checks the vital signs, last updated and onboarding info")
def step_check_vital_onboarding(context):
    user_info = UserBasicInfoPage(context.page)
    user_info.verify_vital_info()
    user_info.verify_last_updated()
    user_info.verify_onboarding_date()

@then("the vital signs, last updated and onboarding info is shown")
def step_vital_onboarding_shown(context):
    print("vital signs, last updated and onboarding info displayed")