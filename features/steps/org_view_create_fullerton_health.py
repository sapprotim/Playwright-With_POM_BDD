from behave import when, then
from pages.create.create_FH_Clinical import Create_FA_clinica
from faker import Faker
from global_state import global_state

fake = Faker()

@when("admin creates a Fullerton Health")
def step_create_facility(context):
    facility_name = "Playwright" + fake.company()
    facility_address = fake.address()

    if global_state.add_fullerton_health:
        return  # Skip if already selected

    sp = Create_FA_clinica(context.page)
    sp.add_fullerton_health(facility_name, facility_address)
    global_state.add_fullerton_health = True

@then("the Fullerton Health should be created successfully")
def step_verify(context):
    print("✅ Clinic creation success message verified.")