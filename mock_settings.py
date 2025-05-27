import sys
import logging
from llama_index.core import (
    Settings, MockEmbedding
)
from llama_index.core.llms.mock import MockLLM
from llama_index.core.callbacks import (
    CallbackManager, TokenCountingHandler
)

def initialize_mock_settings():
    logging.basicConfig(
        stream=sys.stdout, level=logging.INFO
    )  # logging.DEBUG for more verbose output
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

    llm = MockLLM(max_tokens=2048)
    embed_model = MockEmbedding(embed_dim=1536)
    token_counter = TokenCountingHandler(verbose=False)
    callback_manager = CallbackManager([token_counter])

    Settings.llm = llm
    Settings.embed_model = embed_model
    Settings.callback_manager = callback_manager

    return token_counter

def print_token_counts(token_counter):
    print("Prompt LLM token count: ", token_counter.prompt_llm_token_count)
    print("Completion LLM token count: ", token_counter.completion_llm_token_count)
    # print("Embedding token_counts:", token_counter.embedding_token_counts)
    print("Total LLM token count: ", token_counter.total_llm_token_count)

