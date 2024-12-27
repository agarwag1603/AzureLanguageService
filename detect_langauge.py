from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

credential = AzureKeyCredential("")
endpoint=""

text_analytics_client = TextAnalyticsClient(endpoint, credential)

documents = [
    """
    This whole document is written in English. In order for the whole document to be written
    in English, every sentence also has to be written in English, which it is.
    """,
    "Il documento scritto in italiano.",
    "Dies ist in deutsche Sprache verfasst."
]

response = text_analytics_client.detect_language(documents)
result = [doc for doc in response if not doc.is_error]

for doc in result:
    print(f"Language detected: {doc.primary_language.name}")
    print(f"ISO6391 name: {doc.primary_language.iso6391_name}")
    print(f"Confidence score: {doc.primary_language.confidence_score}\n")