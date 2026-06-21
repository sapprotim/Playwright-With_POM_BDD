from behave.__main__ import main as behave_main
import sys

if __name__ == "__main__":
    # List of Doctor  feature files
    feature_files = [
        "features/doctor/doctor_login.feature",
        "features/doctor/user_page_pagination.feature",
        "features/doctor/user_page_filter.feature",
        "features/doctor/user_page_edit.feature",
        "features/doctor/user_page_refresh.feature",
        "features/doctor/user_profile.feature",
        "features/doctor/basic_info.feature",
        "features/doctor/body_info.feature",
        "features/doctor/vital_and_onboarding_info.feature",
        "features/doctor/comparison_click_and_visibility.feature",
        "features/doctor/clinical_params_click_and_check.feature",
        "features/doctor/lifestyle_tab_navigation.feature",
        "features/doctor/lifestyle_params_click_and_check.feature",
        "features/doctor/Calendar_dropdown.feature",
        "features/doctor/trends_comparison_calendar_buttons.feature",
        "features/doctor/verify_trends_generate_wellness_plan_button.feature",
        "features/doctor/patient_log_page_common.feature",
        "features/doctor/patient_logs_calendar.feature",
        "features/doctor/patient_logs_blood_pressure.feature",
        "features/doctor/patient_logs_fasting_blood_glucose.feature",
        "features/doctor/patient_logs_add_or_edit_hba1c.feature",
        "features/doctor/patient_logs_weight_bmi_add_and_edit.feature",
        "features/doctor/patient_logs_WC.feature",
        "features/doctor/patient_logs_lipids_entry.feature",
        "features/doctor/record_page_common.feature",
        "features/doctor/records_refresh.feature",
        "features/doctor/records_upload_document.feature",
        "features/doctor/records_select_document_and_send_message.feature",
        "features/doctor/wp_page_common.feature",
        "features/doctor/WP_generate_wellness_plan.feature",
        "features/doctor/validate_clinical_and_lifestyle_dashboard_score.feature"
    ]
    # Run Behave with the list
    exit_code = behave_main(feature_files)
    sys.exit(exit_code)