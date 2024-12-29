from abc import ABC, abstractmethod
import logging


class LLMError(Exception):
    """Eccezione generica per errori LLM."""
    pass


logger = logging.getLogger(__name__)

class LLMClient(ABC):
    """
    Classe astratta che definisce l'interfaccia minima per interagire
    con un LLM. Include metodi per caricare/configurare il modello,
    generare risposte e gestire eventuali errori.
    """

    @abstractmethod
    def manage_model(self, **kwargs):
        """
        Carica e/o configura il modello LLM.
        """
        pass

    @abstractmethod
    def handle_response(self, prompt: str, context: str) -> str:
        """
        Gestisce una risposta a partire da un prompt.
        """
        pass

    def handle_error(self, error: Exception, operation: str = "") -> None:
        """
        Gestisce gli errori sollevati dal modello o durante la generazione.
        """
        error_msg = f"LLM Error during {operation}" if operation else f"LLM Error: {str(error)}"
        logger.error(error_msg)
        raise LLMError(error_msg)
