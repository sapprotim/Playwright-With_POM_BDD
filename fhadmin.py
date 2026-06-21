from behave.__main__ import main as behave_main
import sys

if __name__ == "__main__":
    # List of feature files
    feature_files = [
        "features/Fullerton_health/fullerton_health_login.feature",
        "features/Fullerton_health/fullerton_health_refresh.feature",

        "features/Fullerton_health/fh_admin_page.feature",
        "features/Fullerton_health/fh_admin_page_refresh.feature",
        "features/Fullerton_health/fh_admin_page_pagination.feature",
        "features/Fullerton_health/fh_admin_sort.feature",
        "features/Fullerton_health/fh_admin_page_search.feature",

        "features/Fullerton_health/clinic_admin_page.feature",
        "features/Fullerton_health/clinic_admin_page_pagination.feature",
        "features/Fullerton_health/clinic_admin_page_refresh.feature",
        "features/Fullerton_health/clinic_admin_page_search.feature",

        "features/Fullerton_health/doctor_page_common.feature",
        "features/Fullerton_health/doctor_page_pagination.feature",
        "features/Fullerton_health/doctor_page_refresh.feature",
        "features/Fullerton_health/doctor_page_search.feature",
        "features/Fullerton_health/doctor_page_edit.feature",
        "features/Fullerton_health/doctor_page_send_pps.feature",

        "features/Fullerton_health/doctor_user_page_common.feature",
        "features/Fullerton_health/doctor_user_page_filter.feature",
        "features/Fullerton_health/doctor_user_page_pagination.feature",
        "features/Fullerton_health/doctor_user_page_refresh.feature",
        "features/Fullerton_health/doctor_user_page_search.feature",

        "features/Fullerton_health/prospect_user_page.feature",
        "features/Fullerton_health/prospect_user_page_calendar.feature",
        "features/Fullerton_health/prospect_user_page_pagination.feature",
        "features/Fullerton_health/prospect_user_page_refresh.feature",
        "features/Fullerton_health/prospect_user_page_search.feature",

        "features/Fullerton_health/users_page.feature",
        "features/Fullerton_health/users_page_filter.feature",
        "features/Fullerton_health/users_page_pagination.feature",
        "features/Fullerton_health/users_page_refresh.feature",
        "features/Fullerton_health/users_page_search.feature",

        "features/Fullerton_health/invite_user_page.feature",
        "features/Fullerton_health/invite_user_page_pagination.feature",
        "features/Fullerton_health/invite_users_page_refresh.feature",
        # "features/Fullerton_health/invite_users_page_reinvite.feature",
        "features/Fullerton_health/invite_users_page_search.feature",

        "features/Fullerton_health/withdrawn_user_page.feature",
        "features/Fullerton_health/withdrawn_user_page_pagination.feature",
        "features/Fullerton_health/withdrawn_users_page_refresh.feature",
        "features/Fullerton_health/withdrawn_users_page_search.feature",

        "features/Fullerton_health/program_completed_user_page.feature",
        "features/Fullerton_health/program_completed_user_page_pagination.feature",
        "features/Fullerton_health/program_completed_user_page_refresh.feature",
        "features/Fullerton_health/program_completed_user_page_search.feature",
        "features/Fullerton_health/programme_completed_user_sort.feature",
        "features/Fullerton_health/programme_completed_user_reset_sort.feature",


        # "features/Fullerton_health/zendesk_user_page.feature",
        # "features/Fullerton_health/zendesk_user_page_pagination.feature",
        # "features/Fullerton_health/zendesk_user_page_search.feature",

        "features/Fullerton_health/user_metrics_page.feature",
        "features/Fullerton_health/user_metrics_page_refresh.feature",
        "features/Fullerton_health/user_metrics_page_calendar.feature",
        "features/Fullerton_health/user_metrics_page_customer_type.feature"

    ]

    # Run Behave with the list
    exit_code = behave_main(feature_files)
    sys.exit(exit_code)