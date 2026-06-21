# QA Automation Suite – BDD & Playwright with POM

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Automation-green?logo=playwright)](https://playwright.dev/)
[![MySQL](https://img.shields.io/badge/MySQL-DB-orange?logo=mysql)](https://www.mysql.com/)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

An **automation test suite** simulating real-user flows for multiple roles:  
Doctor | Clinic Admin | Fullerton Health Admin | Org Admin / HPB Admin

Combines **BDD (Behaviour Driven Development)** with **Playwright UI automation** and a **Page Object Model (POM)** structure. Integrates **MySQL data seeding** so every test run starts clean, seeds data, runs automation, and cleans up.

---

## Features

- BDD (Gherkin) scenarios
- Page Object Model (POM) for reusable test structures
- Playwright browser automation (Chromium, Firefox, WebKit)
- Automatic DB creation, seeding & cleanup
- Role-based flows
- HTML reports via `pytest-html`

---

## Environment Setup

### Runs best on WSL (Windows Subsystem for Linux)

```bash
# Install WSL
wsl --install

# Update packages
sudo apt update && sudo apt upgrade -y

# Install Python & pip
sudo apt install python3 python3-venv python3-pip -y
```

### Setup project

```bash
# Navigate to repo root
# Create & activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
playwright install
```

---

## Credentials Configuration

**Never commit real credentials.** The file `config/credentials.py` is excluded from version control via `.gitignore`.

1. Copy the example file:

```bash
cp config/credentials.example.py config/credentials.py
```

2. Fill in your values in `config/credentials.py`, **or** export them as environment variables:

```bash
export APP_URL="https://your-app-url/#/login"
export ORG_ADMIN_EMAIL="orgadmin@example.com"
export ORG_ADMIN_PASSWORD="YourPassword123!"
export ORG_ADMIN_OTP="000000"
export STM_ADMIN_EMAIL="stmadmin@example.com"
export STM_ADMIN_PASSWORD="YourPassword123!"
export STM_ADMIN_OTP="000000"
export CLINIC_ADMIN_EMAIL="clinicadmin@example.com"
export CLINIC_ADMIN_PASSWORD="YourPassword123!"
export CLINIC_ADMIN_OTP="000000"
export FH_ADMIN_EMAIL="fhadmin@example.com"
export FH_ADMIN_PASSWORD="YourPassword123!"
export FH_ADMIN_OTP="000000"
```

---

## Libraries & Packages

| Purpose            | Packages                |
|--------------------|-------------------------|
| BDD Framework      | `behave`                |
| Browser Automation | `playwright`            |
| Database           | `mysql-connector-python`|
| Dynamic Data       | `faker`                 |
| Image & Fonts      | `Pillow`, `fonttools`   |
| Reports            | `pytest-html`           |
| Utilities          | `python-dotenv`         |

---

## Data Seeding Workflow

1. Create fresh test DB
2. Inject minimal SQL dump
3. Execute automation tests
4. Clean DB after run

All handled automatically with one command.

---

## Running Tests

Run all flows:

```bash
python run_all.py
```

Run a single flow (example: Doctor):

```bash
python3 doctor.py
```

Run a single feature file:

```bash
python3 -m behave features/doctor/WP_generate_wellness_plan.feature
```

---

## Reports

After execution, HTML reports are saved in the `reports/` directory, including:

- Test case results
- Execution time
- Screenshots on failure

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.
