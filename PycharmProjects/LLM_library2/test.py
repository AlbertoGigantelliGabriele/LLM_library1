from mock_client_openai import OpenAIMockClient
import pytest


# from logger import setup_logger
# import logging
# setup_logger(logging.INFO)


def test_openai_mock_generate_response():
    client = OpenAIMockClient()

    # Esempio 1: Parametri validi
    client.manage_model(model_name="openai-mock", version="0.2.0")
    risposta = client.handle_response(prompt="Hello world", context="Test Pydantic + Logging")
    print(risposta)

    # Esempio 2: Parametro non valido (model_name vuoto) => solleva eccezione
    try:
        client.manage_model(model_name="")  # min_length=1 => eccezione
    except Exception as exc:
        print(f"Catturata eccezione: {exc}")


def test_anthropic_mock_generate_response():
    client = OpenAIMockClient()

    client.manage_model(model_name="openai-mock", version="0.2.0")
    risposta = client.handle_response(prompt="Hello world", context="Test Pydantic + Logging")
    print(risposta)

    try:
        client.manage_model(model_name="")
    except Exception as exc:
        print(f"Catturata eccezione: {exc}")


if __name__ == "__main__":
    test_openai_mock_generate_response()
    test_anthropic_mock_generate_response()
