import os

# Copy this file to credentials.py and fill in your values,
# OR set these as environment variables (recommended for CI/CD).

url = os.getenv("APP_URL", "https://your-app-url/#/login")

Org_Admin_email    = os.getenv("ORG_ADMIN_EMAIL", "orgadmin@example.com")
Org_Admin_password = os.getenv("ORG_ADMIN_PASSWORD", "YourPassword123!")
Org_Admin_otp      = os.getenv("ORG_ADMIN_OTP", "000000")

Stm_Admin_email    = os.getenv("STM_ADMIN_EMAIL", "stmadmin@example.com")
Stm_Admin_password = os.getenv("STM_ADMIN_PASSWORD", "YourPassword123!")
Stm_Admin_otp      = os.getenv("STM_ADMIN_OTP", "000000")

clinic_email    = os.getenv("CLINIC_ADMIN_EMAIL", "clinicadmin@example.com")
clinic_password = os.getenv("CLINIC_ADMIN_PASSWORD", "YourPassword123!")
clinic_otp      = os.getenv("CLINIC_ADMIN_OTP", "000000")

fh_email    = os.getenv("FH_ADMIN_EMAIL", "fhadmin@example.com")
fh_password = os.getenv("FH_ADMIN_PASSWORD", "YourPassword123!")
fh_otp      = os.getenv("FH_ADMIN_OTP", "000000")
