import logging
from mock_client_base import LLMClient

logger = logging.getLogger(__name__)


class OpenAIMockClient(LLMClient):

    def __init__(self):
        self.model_name = None

    def manage_model(self, model_name: str = "openai-mock-model", **kwargs):
        try:
            logger.info(f"Loading OpenAI mock model: {model_name}")
            self.model_name = model_name
        except Exception as e:
            self.handle_error(e)

    def handle_response(self, prompt: str) -> str:
        try:
            if not isinstance(prompt, str):
                raise TypeError
            logger.info(f"[OpenAI Mock] Handling response for prompt: {prompt}")
            return f"OpenAI mock response to: {prompt}"
        except Exception as e:
            self.handle_error(e)
