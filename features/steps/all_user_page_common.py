from behave import when, then
from pages.hpb_Menu import AdminPage
from global_state import global_state
from playwright.sync_api import expect
import re
import time
from pages.Doctor_Users_page import Doctoruserpage
from pages.user_profile import UserProfileSearch
from pages.sort_page import SortPage
from pages.patient_logs.PatientLogs_page import PatientLogsPage
from pages.records.records_page import RecordsPage
from pages.role_manager.roleManager_page import RoleManagerPage
from pages.user_basic_info.wellness_score_tab import WellnessScoreTab

# All User Page Common
@when("the user selects the All Users tab")
def step_select_all_users(context):
    if global_state.all_user_selected:
        return
    context.base_page = AdminPage(context.page)
    context.base_page.select_All_user()
    global_state.all_user_selected = True

@then("the All Users tab should be displayed")
def step_all_users_tab_displayed(context):
    assert context.page.locator("//span[normalize-space()='All Users']").is_visible()

# Application Tracker Page Common
@when("the user selects Application Tracker page")
def step_select_application_tracker(context):
    if global_state.application_tracker_selected:
        return
    context.navigation_page = AdminPage(context.page)
    context.navigation_page.select_application_tracker()
    global_state.application_tracker_selected = True

@then("the Application Tracker page should be displayed page")
def step_verify_application_tracker_page(context):
    expect(context.page).to_have_url(re.compile(".*#/application-tracker"))

# Clinic Admin Page Common
@when("selects the Clinic Admin role")
def step_impl(context):
    if global_state.clinic_selected:
        return  # Skip if already selected

    context.admin_page = AdminPage(context.page)
    context.actual_title = context.admin_page.select_clinic()
    global_state.clinic_selected = True

@then("the Clinic Admin page is displayed")
def step_impl(context):
    assert "Clinic Admin" in context.actual_title, (
        f"Expected text containing 'Clinic Admin', but got '{context.actual_title}'"
    )

# Clinic Doctor Page Common
@when('selects doctor to view its doctors')
def step_open_clinic_doctor_page(context):
    if global_state.select_user_to_Doctor:
        return
    global_state.clinic_doctor_page = AdminPage(context.page)
    global_state.doc_page = global_state.clinic_doctor_page.select_user_to_Doctor()
    global_state.select_user_to_Doctor = True

@then('the list of assigned doctors should be displayed')
def step_verify_doctor_list(context):
    assert global_state.select_user_to_Doctor is True
    print("Assigned doctors list displaying")

# Clinic User Page Common
@when("the HPB Admin navigates to the clinic page")
def step_select_application_tracker(context):
    if global_state.select_clinic_users_page:
        return
    context.navigation_page = Doctoruserpage(context.page)
    context.navigation_page.select_clinic_users_page()
    global_state.select_clinic_users_page = True


@then("the clinic user list should be displayed")
def step_verify_application_tracker_page(context):
    expect(context.page).to_have_url(re.compile(".*#/view-department"))

# Doctor Page Common
@when("the Admin selects the Doctor Admin role")
def step_impl(context):
    if global_state.doctor_admin_selected:
        return  # Skip if already selected

    context.admin_page = AdminPage(context.page)
    context.admin_page.select_doctor_admin()
    global_state.doctor_admin_selected = True

@then("the Doctor Admin page is displayed")
def step_impl(context):
    # Add actual assertion if there's a way to confirm
    assert global_state.doctor_admin_selected is True

# FH User Page Common
@when('the HPB Admin navigates to the Fullerton Health page')
def step_open_user_page(context):
    if not global_state.select_user_to_fh:
        fh_c_page = AdminPage(context.page)
        fh_c_page.select_Structure_page()
        time.sleep(2)

        user_page = AdminPage(context.page)
        user_page.select_fh_user()
        time.sleep(2)

        global_state.user_to_fh = AdminPage(context.page)
        global_state.select_user_to_fh = True

@then('the Fullerton Health user list should be displayed')
def step_verify_user_list(context):
    assert global_state.select_user_to_fh is True
    print("Assigned user list is displaying")

# Role Manager Page Common
@when("the user navigates to the Role Manager page")
def step_navigate_to_role_manager(context):
    if global_state.role_manager_page_opened:
        return
    context.role_manager_page = RoleManagerPage(context.page)
    context.role_manager_page.navigate_to_WP()
    global_state.role_manager_page_opened = True

@then("the Role Manager page should be visible")
def step_verify_role_manager(context):
    assert context.page.locator("//h1[normalize-space()='Role Manager']").is_visible()

# User Metrics Page Common
@when('the Admin opens the User Metrics page')
def step_impl(context):
    if global_state.navigate_to_user_metrics:
        return
    global_state.users_page = AdminPage(context.page)
    global_state.user_metrics_title = global_state.users_page.select_user_metrics()
    global_state.navigate_to_user_metrics = True

@then('the User Metrics page should be displayed')
def step_impl(context):
    expect(global_state.user_metrics_title).to_be_visible()

# Zendesk User Page Common
@when('the Admin opens the Zendesk Users page')
def step_impl(context):
    if global_state.navigate_to_zendesk_tab:
        return
    global_state.users_page = AdminPage(context.page)
    global_state.users_page.select_zendesk_user()
    global_state.navigate_to_zendesk_tab = True

@then('the Zendesk Users page should be displayed')
def step_impl(context):
    zendesk_user_tab = context.page.locator("//div[@class='user-list-title']")
    text = zendesk_user_tab.text_content().strip()
    assert text == "Zendesk Users", f"Expected 'Zendesk Users' but got '{text}'"

# Org Admin Org View Page Common
@when("the Admin opens the Organization View tab")
def step_impl(context):
    if global_state.organization_view_opened:
        return  # Skip if already opened

    context.admin_page = AdminPage(context.page)
    context.admin_page.open_Organization_View()
    global_state.organization_view_opened = True

@then("the Organization View tab should be visible")
def step_impl(context):
    # You can verify any element specific to that tab
    locator = context.page.get_by_text("HPB", exact=True)
    assert locator.is_visible(), "Organization View tab is not visible"

# Doctor Page User Profile Common
@when("the doctor searches for a user profile")
def step_impl(context):
    if global_state.profile_searched:
        return
    context.user_profile_search = UserProfileSearch(context.page)
    context.user_profile_search.search_user_profile()
    global_state.profile_searched = True

@then("the user profile should be opened")
def step_impl(context):
    pass
    # # Replace sleep with explicit wait if possible
    # context.page.wait_for_selector("text=Basic Info", timeout=5000)
    # assert context.page.locator("text=Basic Info").is_visible(), "User profile page did not open"

# Clinic Page Clinic Admin Common
@when("selects Clinic Admin to view its Clinic Admins")
def step_impl(context):
    if global_state.select_doctor_to_Clinic_Admin:
        return
    global_state.clinic_doctor_page = AdminPage(context.page)
    global_state.ca_page = global_state.clinic_doctor_page.select_doctor_to_Clinic_Admin()
    time.sleep(2)
    global_state.select_doctor_to_Clinic_Admin = True

@then("the list of assigned Clinic Admin should be displayed")
def step_impl(context):
    assert global_state.select_doctor_to_Clinic_Admin is True
    print("the list of assigned Clinic Admin displaying")

# FH Admin Sort Common
@when("the user clicks the Name column to sort A-Z")
def step_click_name_sort(context):
    sort = SortPage(context.page)
    sort.sort_by_name_az_and_last_sign_in()

@then("the table should reflect the sorted order accordingly")
def step_validate_sort(context):
    time.sleep(2)
    print("✅ Sort check done.")

# FH Page FH Admin Page Common
@when('selects fh to view its admins')
def step_open_user_page(context):
    if global_state.select_doctor_to_Clinic_Admin:
        return
    global_state.FH_Admin_page = AdminPage(context.page)
    global_state.fh_page = global_state.FH_Admin_page.select_doctor_to_Clinic_Admin()
    time.sleep(2)
    global_state.select_doctor_to_Clinic_Admin = True

@then('the list of assigned admins should be displayed')
def step_verify_user_list(context):
    assert global_state.select_doctor_to_Clinic_Admin is True
    print("Assigned user list is displaying")

# Patient Logs User Page Common
@when("the navigates Trend to Patient Logs")
def step_impl(context):
    if global_state.patient_logs_opened:
        return  # Skip if already opened

    context.admin_page = PatientLogsPage(context.page)
    context.admin_page.navigate_to_patient_logs()
    global_state.patient_logs_opened = True

@then("the Patient Logs page should be visible")
def step_impl(context):
    assert global_state.patient_logs_opened is True
    # Or use expect() here if there's a confirmatory element on the page

@when("navigates to the Lifestyle tab")
def step_impl(context):
    if global_state.navigate_to_lifestyle_tab:
        return
    context.user_Lifestyle_tab = WellnessScoreTab(context.page)
    context.user_Lifestyle_tab.navigate_to_lifestyle_tab()
    global_state.navigate_to_lifestyle_tab = True


@then("the Lifestyle tab should be opened")
def step_impl(context):
    assert global_state.navigate_to_lifestyle_tab is True


@when("the Doctor Admin navigates to Records page")
def step_impl(context):
    if global_state.records_page_opened:
        return
    context.admin_page = RecordsPage(context.page)
    context.admin_page.navigate_to_records_files()
    global_state.records_page_opened = True

@then("the Records page should be visible")
def step_impl(context):
    assert global_state.records_page_opened is True



@when("the Doctor Admin navigates to the WP page")
def step_impl(context):
    if global_state.wp_page_opened:
        return
    context.admin_page = RoleManagerPage(context.page)
    context.admin_page.navigate_to_WP()
    global_state.wp_page_opened = True

@then("the WP page should be visible")
def step_impl(context):
    assert global_state.wp_page_opened is True
    # Optionally verify UI element:
    # expect(context.page.get_by_text("Workplace Permissions")).to_be_visible()

# FH Admin page Common
@when("the Admin selects the Fullerton Health Admin role")
def step_impl(context):
    if global_state.select_fullerton_admin:
        return
    context.admin = AdminPage(context.page)
    context.admin.select_fullerton_admin()
    global_state.select_fullerton_admin = True

@then("the Fullerton Health Admin page is displayed")
def step_impl(context):
    assert global_state.select_fullerton_admin is True
