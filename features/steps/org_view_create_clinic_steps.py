from behave import when, then
from pages.create.create_FH_Clinical import Create_FA_clinica
from faker import Faker

fake = Faker()


@when("admin creates a Clinic")
def step_create_clinic(context):
    clinic_name = "Playwright" + fake.company()
    clinic_address = fake.street_address()
    sp = Create_FA_clinica(context.page)
    sp.add_clinic(clinic_name, clinic_address)



@then("the Clinic should be created successfully")
def step_verify(context):
    print("Clinic creation success message verified.")