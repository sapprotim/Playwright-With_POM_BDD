from behave.__main__ import main as behave_main
import sys

if __name__ == "__main__":
    # List of feature files
    feature_files = [
        # ORG ADMIN LOGIN
        "features/org_admin/org_admin_login.feature",

        # HPB » STRUCTURE
        # Fullerton Health & Clinic + Organization View
        "features/org_admin/org_view_fh_and_clinic_count.feature",
        "features/org_admin/org_view_search.feature",
        "features/org_admin/org_view_refresh.feature",
        "features/org_admin/org_view_pagination.feature",
        "features/org_admin/org_view_create_fullerton_health.feature",
        "features/org_admin/org_view_create_clinic.feature",
        "features/org_admin/org_view_delete_clinic.feature",
        "features/org_admin/org_view_delete_fullerton_health.feature",
        "features/org_admin/org_view_refresh.feature",

        # Clinic (page)
        "features/org_admin/clinic_user_page_common.feature",
        "features/org_admin/clinic_user_page_search.feature",
        "features/org_admin/clinic_user_page_refresh.feature",
        "features/org_admin/clinic_users_assign.feature",
        "features/org_admin/clinic_users_pagination.feature",
        "features/org_admin/clinic_users_edit.feature",

        # Clinic Doctor (page)
        "features/org_admin/clinic_doctor_page_common.feature",
        "features/org_admin/clinic_doctor_page_search.feature",
        "features/org_admin/clinic_doctor_page_refresh.feature",
        # "features/org_admin/clinic_doctor_page_pagination.feature",
        "features/org_admin/clinic_doctor_page_edit.feature",

        # Clinic Page, Clinic Admin
        "features/org_admin/clinic_page_clinic_admin_common.feature",
        "features/org_admin/clinic_page_clinic_admin_search.feature",
        "features/org_admin/clinic_page_clinic_admin_refresh.feature",
        "features/org_admin/clinic_page_clinic_admin_assign.feature",
        # "features/org_admin/clinic_page_clinic_admin_pagination.feature",
        "features/org_admin/clinic_page_clinic_admin_edit.feature",

        # FH Users
        "features/org_admin/fh_user_page_common.feature",
        "features/org_admin/fh_user_page_search.feature",
        "features/org_admin/fh_user_page_refresh.feature",
        # "features/org_admin/fh_user_page_pagination.feature",
        "features/org_admin/fh_user_page_edit.feature",

        # FH Doctors
        "features/org_admin/fh_doctor_page_common.feature",
        "features/org_admin/fh_doctor_page_search.feature",
        "features/org_admin/fh_doctor_page_refresh.feature",
        # "features/org_admin/fh_doctor_page_pagination.feature",
        "features/org_admin/fh_doctor_page_edit.feature",

        # FH, FH Admin (page)
        "features/org_admin/fh_page_fh_admin_common.feature",
        "features/org_admin/fh_page_fh_admin_search.feature",
        "features/org_admin/fh_page_fh_admin_refresh.feature",
        "features/org_admin/fh_page_fh_admin_assign.feature",
        # "features/org_admin/fh_page_fh_admin_pagination.feature",
        "features/org_admin/fh_page_fh_admin_edit.feature",

        # HPB » HPB ADMIN
        "features/org_admin/hpb_admin_page_common.feature",
        "features/org_admin/hpb_admin_page_pagination.feature",
        "features/org_admin/hpb_admin_page_search.feature",

        # HPB » FULLERTON HEALTH ADMIN
        # FH Admin (main)
        "features/org_admin/fh_admin_page.feature",
        "features/org_admin/fh_admin_page_search.feature",
        "features/org_admin/fh_admin_page_pagination.feature",
        "features/org_admin/fh_admin_page_refresh.feature",
        "features/org_admin/fh_admin_page_fh_admin_create.feature",
        # "features/org_admin/fh_admin_page_edit.feature",
        "features/org_admin/fh_admin_page_delete.feature",
        "features/org_admin/fh_admin_sort.feature",

        # HPB » CLINIC ADMIN
        # Clinic Admin (main)
        "features/org_admin/clinic_admin_page.feature",
        "features/org_admin/clinic_admin_page_search.feature",
        "features/org_admin/clinic_admin_page_pagination.feature",
        "features/org_admin/clinic_admin_page_refresh.feature",
        "features/org_admin/clinic_admin_page_clinic_admin_create.feature",
        "features/org_admin/clinic_admin_page_edit.feature",
        "features/org_admin/clinic_admin_page_delete.feature",

        # HPB » DOCTOR
        # Org-level doctors
        "features/org_admin/doctor_page_common.feature",
        "features/org_admin/doctor_page_search.feature",
        "features/org_admin/doctor_page_pagination.feature",
        "features/org_admin/doctor_page_refresh.feature",
        "features/org_admin/doctor_page_doctor_create.feature",
        "features/org_admin/doctor_page_doctor_edit.feature",
        "features/org_admin/doctor_page_doctor_delete.feature",
        "features/org_admin/doctor_page_edit.feature",

        # Doctor » Associated Users
        "features/org_admin/doctor_user_page_common.feature",
        "features/org_admin/doctor_user_page_pagination.feature",
        "features/org_admin/doctor_user_page_search.feature",
        "features/org_admin/doctor_user_page_refresh.feature",
        "features/org_admin/doctor_user_page_filter.feature",

        # HPB » USERS
        # Prospects
        "features/org_admin/prospect_user_page.feature",
        "features/org_admin/prospect_user_page_calendar.feature",
        "features/org_admin/prospect_user_page_pagination.feature",
        "features/org_admin/prospect_user_page_refresh.feature",
        "features/org_admin/prospect_user_page_search.feature",

        # Users » Assigned Users
        "features/org_admin/users_page.feature",
        "features/org_admin/users_page_filter.feature",
        "features/org_admin/users_page_pagination.feature",
        "features/org_admin/users_page_refresh.feature",
        "features/org_admin/users_page_search.feature",

        # Users » All Users
        "features/org_admin/all_user_page.feature",
        # "features/org_admin/all_user_page_pagination.feature",
        "features/org_admin/all_users_page_refresh.feature",
        "features/org_admin/all_users_page_search.feature",

        # Users » Invited Users
        "features/org_admin/invite_user_page.feature",
        # "features/org_admin/invite_user_page_pagination.feature",
        "features/org_admin/invite_users_page_refresh.feature",
        # "features/org_admin/invite_users_page_reinvite.feature",
        "features/org_admin/invite_users_page_search.feature",



        # Users » Withdrawn Users
        "features/org_admin/withdrawn_user_page.feature",
        # "features/org_admin/withdrawn_user_page_pagination.feature",
        "features/org_admin/withdrawn_users_page_refresh.feature",
        "features/org_admin/withdrawn_users_page_search.feature",

        # Users » User Metrics
        "features/org_admin/user_metrics_page.feature",
        "features/org_admin/user_metrics_page_calendar.feature",
        "features/org_admin/user_metrics_page_customer_type.feature",
        "features/org_admin/user_metrics_page_refresh.feature",

        # APPLICATION TRACKER
        "features/org_admin/application_tracker_page_common.feature",
        "features/org_admin/application_tracker_page_calendar.feature",
        "features/org_admin/application_tracker_page_more_view.feature",
        "features/org_admin/application_tracker_page_pagination.feature",
        "features/org_admin/application_tracker_page_refresh.feature",
        "features/org_admin/application_tracker_engagemant_page.feature",
        "features/org_admin/application_tracker_engagemant_page_mobile.feature",
        "features/org_admin/application_tracker_engagemant_page_web.feature",

        # ROLE MANAGER
        "features/org_admin/role_manager_page.feature",
        "features/org_admin/role_manager_page_custom_role_checkbox_in.feature",
        "features/org_admin/role_manager_page_custom_role_checkbox_out.feature",
        "features/org_admin/role_manager_page_custom_role_create.feature",
        "features/org_admin/role_manager_page_custom_role_edit.feature",
        "features/org_admin/role_manager_page_custom_role_delete.feature",
        "features/org_admin/role_manager_page_default_checkbox_in.feature",
        "features/org_admin/role_manager_page_default_checkbox_out.feature"
]
    # Run Behave with the list
    exit_code = behave_main(feature_files)
    sys.exit(exit_code)