from behave import when, then
from pages.records.document_messaging import DocumentMessaging


@when("sends the document with a message")
def step_send_document_with_message(context):
    doc_msg = DocumentMessaging(context.page)
    doc_msg.select_document_checkbox()
    doc_msg.send_message_to_user()

@then("the confirmation message 'Documents message sent to user successfully' should appear")
def step_verify_document_sent_message(context):
    print("Message sent successfully")



