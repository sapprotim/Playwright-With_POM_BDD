from behave import given, when, then
from pages.Filter import Filter
from playwright.sync_api import sync_playwright


@when("the admin applies the filter")
def step_apply_normal_filter(context):
    user_page = Filter(context.page)
    user_page.click_Filter()
    user_page.select_clinic_normal()
    user_page.select_all_date()
    user_page.select_BP_Logged()
    user_page.click_done()
    user_page.cancel_filter()
    user_page.page.reload()

@then("the system should display filtered results matching selected criteria")
def step_validate_filtered_results(context):
    page = Filter(context.page)
    page.filter_validation(0)
    page.page.reload()

@when("the admin filters users by clinic")
def step_apply_normal_filter(context):
    user_page = Filter(context.page)
    user_page.click_Filter()
    user_page.select_clinic_normal()
    user_page.click_done()

@then("the filtered users should be displayed correctly")
def step_validate_filtered_results(context):
    page = Filter(context.page)
    page.filter_validation_doctor_user(0)
    page.page.reload()



@when("the fh filters for users")
def step_apply_normal_filter(context):
    user_page = Filter(context.page)
    user_page.click_Filter()
    user_page.select_clinic_normal()
    user_page.select_all_date()
    user_page.click_done()
    user_page.select_BP_Logged()
    user_page.click_done()


@then("the fh filtered users should be displayed correctly")
def step_validate_filtered_results(context):
    page = Filter(context.page)
    page.filter_validation(0)
    page.page.reload()



