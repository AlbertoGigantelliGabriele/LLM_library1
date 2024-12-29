import logging
from abc import ABC

from mock_client_base import LLMClient

logger = logging.getLogger(__name__)


class AnthropicMockClient(LLMClient, ABC):

    def __init__(self):
        self.model_name = None

    def manage_model(self, model_name: str = "anthropic-mock-model"):
        try:
            logger.info(f"Loading Anthropic mock model: {model_name}")
            self.model_name = model_name
        except Exception as e:
            self.handle_error(e)

    def handle_response(self, prompt: str) -> str:
        try:
            logger.info(f"[Anthropic Mock] Generating response for prompt: {prompt}")
            return f"Anthropic mock response to: {prompt}"
        except Exception as e:
            self.handle_error(e)
