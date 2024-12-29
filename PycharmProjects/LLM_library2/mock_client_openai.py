import logging
from validation_models import PromptInput, LLMResponse, ModelConfig
from mock_client_base import LLMClient


logger = logging.getLogger(__name__)

class OpenAIMockClient(LLMClient):

    def __init__(self):
        self.model_name = None
        self.model_version = None

    def manage_model(self, model_name: str = "openai-mock-model", **kwargs):

        try:
            params = {'model_name': model_name, **kwargs}
            config = ModelConfig(**params)
            logger.info(f"Loading OpenAI mock model: {model_name}")

            self.model_name = model_name
            self.model_version = config.version

            logger.info(f"Modello '{self.model_name}' (version: {self.model_version}) caricato con successo.")

        except Exception as e:
            # Se Pydantic non valida i dati o se c'è un errore generico
            self.handle_error(e, "managing model")

    def handle_response(self, prompt: str, context: str) -> str:

        PromptInput(prompt=prompt, context=context)
        mock_result = f"\nOpenAI mock response to: {prompt} with context: {context}"
        output_data = LLMResponse(response=mock_result)

        logger.info(f"[OpenAI Mock] Generating response for prompt: {prompt}, context: {context}")

        return output_data.response
