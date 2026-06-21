from behave import when, then
import time
from pages.Filter import Filter  # Make sure the import path and class name are correct

@when("the doctor filters users by clinic")
def step_impl(context):
    filter_page = Filter(context.page)   # instantiate Filter with the Playwright page
    filter_page.click_Filter()
    filter_page.select_clinic_Myuser()
    filter_page.select_medical()
    filter_page.select_program()
    filter_page.select_all_date()
    filter_page.click_done()

@then("the filtered result should be displayed correctly")
def step_impl(context):
    filter_page = Filter(context.page)
    filter_page.filter_validation_doctor_user(0)
    time.sleep(2)
    filter_page.cancel_filter()
    filter_page.page.reload()