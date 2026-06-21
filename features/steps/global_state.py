login_done = False


class GlobalState:
    def __init__(self):
        self.login_done = False
        self.profile_searched = False
        self.select_clinic_users_page = False
        self.add_fullerton_health = False
        self.add_clinic = False
        self.clinic_name = None
        self.facility_name = None
        self.select_user_to_Doctor = False
        self.select_doctor_to_Clinic_Admin = False
        self.select_user_to_fh = False
        self.select_doctor_to_Clinic_Admin = False
        self.organization_view_opened = False
        self.select_fullerton_admin = False
        self.clinic_selected = False
        self.doctor_admin_selected = False
        self.patient_logs_opened = False
        self.records_page_opened = False
        self.navigate_to_lifestyle_tab = False
        self.wp_page_opened = False
        self.doctor_user_selected = False
        self.navigate_to_prospects_user = False
        self.navigate_to_users_tab = False
        self.navigate_to_zendesk_tab = False
        self.navigate_to_user_metrics = False
        self.hpb_admin_selected = False
        self.fh_admin_created = False
        self.clinic_admin_created = False
        self.doctor_created = False
        self.invite_user_selected = False
        self.withdrawn_user_selected = False
        self.all_user_selected = False
        self.role_manager_page_opened = False
        self.custom_role_created = False
        self.application_tracker_selected = False
        self.engagements_selected = False
        self.add_fullerton_health = False
        self.select_programme_completed_user = False

global_state = GlobalState()
