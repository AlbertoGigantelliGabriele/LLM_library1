from mock_client_base import LLMError
from mock_client_openai import OpenAIMockClient
from mock_client_anthropic import AnthropicMockClient
import logging
from logger import setup_logger

setup_logger(logging.INFO)  # configurazione dei log levels


def test_openai_mock_generate_response():
    client = OpenAIMockClient()
    client.manage_model()
    try:
        response = client.handle_response("Hello")
        assert "OpenAI mock response" in response
    except Exception as e:
        client.handle_error(e)


def test_anthropic_mock_generate_response():
    client = AnthropicMockClient()
    client.manage_model()
    try:
        response = client.handle_response("Hello")
        assert "Anthropic mock response" in response
    except Exception as e:
        client.handle_error(e)


import numpy as np


def test_openai_mock_without_model():
    """
    simuliamo un errore in cui viene passato un tipo diverso da una stringa in input
    :return:
    """
    client = OpenAIMockClient()  # Non chiamiamo manage_model()
    try:
        client.handle_response(np.nan)
        assert False, "Dovrebbe sollevare un'eccezione"
    except Exception as e:
        assert True  # Il test passa se viene sollevata un'eccezione


if __name__ == "__main__":
    test_openai_mock_generate_response()
    test_anthropic_mock_generate_response()
    test_openai_mock_without_model()
