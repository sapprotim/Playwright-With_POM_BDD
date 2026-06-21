from playwright.sync_api import sync_playwright
import os
from datetime import datetime

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.context = context.browser.new_context(viewport={"width": 1920, "height": 1080})
    context.context.set_default_timeout(20000)
    context.page = context.context.new_page()

def before_scenario(context, scenario):
    if hasattr(context, "page"):
        context.page.bring_to_front()
    else:
        context.page = context.context.new_page()

def after_scenario(context, scenario):
    if scenario.status == "failed":
        os.makedirs("screenshots", exist_ok=True)
        path = f"screenshots/{scenario.name.replace(' ', '_')}_FAILED_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        context.page.screenshot(path=path, full_page=True)
        print(f"❌ Scenario failed. Screenshot saved to: {path}")

def after_all(context):
    if hasattr(context, "page"):
        context.page.close()
    context.context.close()
    context.browser.close()
    context.playwright.stop()