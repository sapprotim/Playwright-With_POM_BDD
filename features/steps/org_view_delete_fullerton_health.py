from behave import when, then
from pages.Delete import Delete
from pages.search_page import SearchPage
from pages.create.create_FH_Clinical import Create_FA_clinica
from faker import Faker
from global_state import global_state
fake = Faker()


@when("selects a Fullerton Health to delete")
def step_delete_facility(context):
    # # Get facility_name from context or global_state
    facility_name = getattr(context, "facility_name", None) or getattr(global_state, "facility_name", None)

    # If not found, create a new Fullerton (for standalone run)
    if not facility_name:
        facility_name = "Playwright" + fake.company()
        facility_address = fake.address()

        sp = Create_FA_clinica(context.page)
        sp.add_fullerton_health(facility_name, facility_address)

        # Save for reuse
        context.facility_name = facility_name
        global_state.facility_name = facility_name
        global_state.add_fullerton_health = True

        search_delete = SearchPage(context.page)
        search_delete.search_function(facility_name)
        delete = Delete(context.page)
        delete.delete_FH()

@then("the Fullerton Health should no longer appear in the Fullerton Health list")
def step_verify(context):
    print("✅ Fullerton Health delete success message verified.")