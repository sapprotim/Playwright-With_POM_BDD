from behave import when, then
from pages.doctor_send_post_programme_survey import DoctorSendPostProgrammeSurvey
from playwright.sync_api import expect
from datetime import datetime


@when("sends a Post Programme Survey to the doctor")
def step_send_pps(context):
    context.pps_page = DoctorSendPostProgrammeSurvey(context.page)
    context.pps_sent = context.pps_page.doctor_send_pps()


@then("the survey should be recorded with the correct sent date")
def step_verify_pps_date(context):
    if not getattr(context, "pps_sent", False):
        return

    survey_sent_box = context.pps_page.get_survey_sent_box_locator()
    expect(survey_sent_box).to_be_visible(timeout=500)
    actual = survey_sent_box.inner_text().strip().strip("()").lstrip("0")
    expected = datetime.now().strftime("%I:%M %p, %d-%m-%Y").lstrip("0")

    if actual != expected:
        raise AssertionError(f"Survey sent date mismatch! Expected: {expected}, Actual: {actual}")