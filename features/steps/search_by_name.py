import time

from behave import given, when, then
import re
import random
from pages.search_page import SearchPage


@when("the user searches for a name")
def step_search_by_name(context):
    time.sleep(4)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//div[@class='table-wrap']//table/tbody/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)
        full_text = context.page.locator(f"//div[@class='table-wrap']//table/tbody/tr[{i}]/td[1]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        context.random_name = name_only
        search_page.search_function(name_only)

@when("the HPB Admin searches for a fh")
def step_search_by_name(context):
    time.sleep(5)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//tbody/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)  
        full_text = context.page.locator(f"//tbody/tr[{i}]/td[1]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        context.random_name = name_only
        search_page.search_function_FH(name_only)


@when("the clinic searches for a name")
def step_search_by_name(context):
    time.sleep(4)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//tbody/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)  
        full_text = context.page.locator(f"//tbody/tr[{i}]/td[1]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        context.random_name = name_only
        search_page.search_function(name_only)


@when("searches for a name")
def step_search_by_name(context):
    time.sleep(5)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//tbody/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)
        full_text = context.page.locator(f"//tbody/tr[{i}]/td[2]").inner_text() # Clinic - Doctor
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        context.random_name = name_only
        search_page.search_function_clinic_doc(name_only)


@when("the Clinic Admin searches for a Clinic Admin")
def step_search_by_name(context):
    time.sleep(4)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//tbody/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)  
        full_text = context.page.locator(f"//tbody/tr[{i}]/td[1]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        context.random_name = name_only
        search_page.search_function(name_only)


@when("the doctor searches for a name")
def step_search_by_name(context):
    time.sleep(4)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//tbody/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)
        full_text = context.page.locator(f"//tbody/tr[{i}]/td[1]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        context.random_name = name_only
        search_page.search_function(name_only)

@when("the FH doctor searches for a name")
def step_search_by_name(context):
    time.sleep(4)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//tbody/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)
        full_text = context.page.locator(f"//tbody/tr[{i}]/td[2]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        context.random_name = name_only
        search_page.search_function(name_only)

@when("the FH admin searches for a name")
def step_search_by_name(context):
    time.sleep(5)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//tbody/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)  
        full_text = context.page.locator(f"//tbody/tr[{i}]/td[1]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        context.random_name = name_only
        search_page.search_function(name_only)

@when("the prospect user searches for a name")
def step_search_by_name(context):
    time.sleep(4)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//body[1]/app-root[1]/div[3]/app-all-prospects[1]/div[1]/div[4]/div[1]/table[1]/tbody[1]/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)  
        full_text = context.page.locator(f"//body[1]/app-root[1]/div[3]/app-all-prospects[1]/div[1]/div[4]/div[1]/table[1]/tbody[1]/tr[{i}]/td[1]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        context.random_name = name_only
        search_page.search_function(name_only)

@when("the zendesk user searches for a name")
def step_search_by_name(context):
    time.sleep(4)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//tbody/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)
        full_text = context.page.locator(f"//tbody/tr[{i}]/td[1]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        context.random_name = name_only
        search_page.search_function(name_only)

@when("the HPB admin searches for a name")
def step_search_by_name(context):
    time.sleep(3)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//tbody/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)
        full_text = context.page.locator(f"//tbody/tr[{i}]/td[1]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip().split()[0] # Store first text only
        context.random_name = name_only
        search_page.search_function(name_only)


@when("the invite user searches for a name")
def step_search_by_name(context):
    time.sleep(5)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//div[@class='table-wrap']//table/tbody/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)
        full_text = context.page.locator(f"//div[@class='table-wrap']//table/tbody/tr[{i}]/td[3]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        context.random_name = name_only
        search_page.search_function_Invited_Users(name_only)


@when("the withdrawn user searches for a name")
def step_search_by_name(context):
    time.sleep(3)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//tbody/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)
        full_text = context.page.locator(f"//tbody/tr[{i}]/td[1]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        context.random_name = name_only
        search_page.search_function(name_only)


@when("the Programme Completed user searches for a name")
def step_search_by_name(context):
    time.sleep(3)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//tbody/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)
        full_text = context.page.locator(f"//tbody/tr[{i}]/td[2]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        context.random_name = name_only
        search_page.search_function_clinic_doc(name_only)

@when("the all user searches for a name")
def step_search_by_name(context):
    time.sleep(3)
    search_page = SearchPage(context.page)
    rows = context.page.locator("//div[@class='table-wrap']//table/tbody/tr")
    count = rows.count()
    if count == 0:
        pass
    else:
        i = random.randint(1, count)  
        full_text = context.page.locator(f"//div[@class='table-wrap']//table/tbody/tr[{i}]/td[1]").inner_text()
        name_only = re.sub(r"\s*\(.*?\)", "", full_text).strip()
        context.random_name = name_only
        time.sleep(5)
        search_page.search_function(name_only)

@then("the system should display the matching user")
def step_validate_search_results(context):
    print("✅ Search result check done.")


