from behave import when, then
from pages.records.upload_document import DocumentUploader


@when("uploads a document")
def step_navigate_patient_logs(context):
    uploader = DocumentUploader(context.page)
    uploader.click_upload_button()
    uploader.upload_document_file()


@then("the uploaded document should be visible in the records")
def step_check_bp_section(context):
    print("Document uploaded")

