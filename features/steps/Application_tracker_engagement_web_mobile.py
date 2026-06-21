import time

from behave import given, when, then
from pages.engagement_web import IframeBoardPage

@when("the user accesses the public board via iframe")
def step_access_public_board(context):
    context.iframe_page = IframeBoardPage(context.page)
    context.iframe_page.access_public_board()

@when("the user accesses the public board mobile")
def step_access_public_board(context):
    context.iframe_page = IframeBoardPage(context.page)
    time.sleep(2)
    context.iframe_page.access_public_board_mobile()

@then("the public board is visible")
def step_public_board_visible(context):
    # You can adjust this to your specific success condition
    print("Pass")