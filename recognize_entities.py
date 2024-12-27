from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

credential = AzureKeyCredential("")
endpoint=""

text_analytics_client = TextAnalyticsClient(endpoint, credential)

documents = [
    """
    Microsoft was founded by Bill Gates and Paul Allen. Its headquarters are located in Redmond. Redmond is a
    city in King County, Washington, United States, located 15 miles east of Seattle.
    """,
    "Jeff bought three dozen eggs because there was a 50% discount."
]

response = text_analytics_client.recognize_entities(documents, language="en")
result = [doc for doc in response if not doc.is_error]

for doc in result:
    for entity in doc.entities:
        print(f"Entity: {entity.text}")
        print(f"...Category: {entity.category}")
        print(f"...Confidence Score: {entity.confidence_score}")
        print(f"...Offset: {entity.offset}")