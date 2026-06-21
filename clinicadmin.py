from behave.__main__ import main as behave_main
import sys

if __name__ == "__main__":
    # List of CA  feature files
    feature_files = [
        "features/clinic_admin/clinic_login.feature",
        "features/clinic_admin/user_page_refresh.feature",
        "features/clinic_admin/user_page_pagination.feature",
        "features/clinic_admin/clinic_user_filter.feature",
        "features/clinic_admin/clinic_user_sort.feature",
        "features/clinic_admin/clinic_user_reset_sort.feature",
        "features/clinic_admin/clinic_user_search_by_name.feature",
        "features/clinic_admin/org_view_common.feature",
        "features/clinic_admin/org_view_page_refresh.feature",
        "features/clinic_admin/clinic_admin_page.feature",
        "features/clinic_admin/clinic_admin_page_pagination.feature",
        "features/clinic_admin/clinic_admin_page_refresh.feature",
        "features/clinic_admin/clinic_admin_page_search.feature",
        "features/clinic_admin/clinic_admin_page_sort.feature",
        "features/clinic_admin/doctor_page_common.feature",
        "features/clinic_admin/doctor_page_pagination.feature",
        "features/clinic_admin/doctor_page_search.feature",
        # "features/clinic_admin/doctor_page_edit.feature",
        "features/clinic_admin/doctor_page_refresh.feature",
        "features/clinic_admin/doctor_page_sort.feature",
        "features/clinic_admin/doctor_user_page_common.feature",
        "features/clinic_admin/doctor_user_page_pagination.feature",
        "features/clinic_admin/doctor_user_page_search.feature",
        "features/clinic_admin/doctor_user_page_refresh.feature",
        "features/clinic_admin/doctor_user_page_filter.feature",
    ]

    # Run Behave with the list
    exit_code = behave_main(feature_files)
    sys.exit(exit_code)