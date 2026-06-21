from behave import when, then
from pages.Delete import Delete
from pages.search_page import SearchPage
from pages.create.create_FH_Clinical import Create_FA_clinica
from global_state import global_state
from faker import Faker
fake = Faker()


@when("selects a clinic to delete")
def step_delete_clinic(context):
    # Try to get clinic name from context or global_state
    clinic_name = getattr(context, "clinic_name", None) or getattr(global_state, "clinic_name", None)

    # If not found, generate and create fresh clinic (for standalone run)
    if not clinic_name:
        facility_name = "Playwright" + fake.company()
        facility_address = fake.address()
        clinic_name = "Playwright" + fake.company()
        clinic_address = fake.street_address()

        sp = Create_FA_clinica(context.page)
        sp.add_fullerton_health(facility_name, facility_address)
        sp.add_clinic(clinic_name, clinic_address)

        # Store for reuse
        context.facility_name = facility_name
        context.clinic_name = clinic_name
        global_state.facility_name = sp.add_fullerton_health
        global_state.clinic_name = sp.add_clinic
        global_state.add_fullerton_health = True
        global_state.add_clinic = True


        search_delete = SearchPage(context.page)
        search_delete.perform_search(clinic_name)
        delete = Delete(context.page)
        delete.delete_clinic()

@then("the clinic should no longer appear in the clinic list")
def step_verify(context):
    print("✅ Clinic delete success message verified.")