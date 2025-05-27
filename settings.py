import os
import sys
import logging
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.core import Settings

def initialize_settings(azure_api_key=None):
    logging.basicConfig(
        stream=sys.stdout, level=logging.WARNING
    )  # logging.DEBUG for more verbose output
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

    if azure_api_key is None:
        api_key = os.getenv("AZURE_OPEN_API_KEY")
    else:
        api_key = azure_api_key
    azure_endpoint = "https://haral-m9l329ou-eastus2.cognitiveservices.azure.com/"
    api_version = "2024-12-01-preview"

    llm = AzureOpenAI(
        model="gpt-35-turbo",
        deployment_name="gpt-35-turbo",
        api_key=api_key,
        azure_endpoint=azure_endpoint,
        api_version=api_version,
    )

    embed_model = AzureOpenAIEmbedding(
        model="text-embedding-ada-002",
        deployment_name="text-embedding-ada-002",
        api_key=api_key,
        azure_endpoint=azure_endpoint,
        api_version=api_version,
    )

    Settings.llm = llm
    Settings.embed_model = embed_model
