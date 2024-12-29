from abc import ABC, abstractmethod
import logging


class LLMError(Exception):
    """Eccezione generica per errori LLM."""
    # Questa classe può avere un modulo suo se aumenta di complessità
    pass


logger = logging.getLogger(__name__)


class LLMClient(ABC):
    """
    Classe astratta che definisce l'interfaccia minima per interagire
    con un LLM. Include metodi per caricare/configurare il modello,
    gestire risposte ed eventuali errori.
    """

    @abstractmethod
    def manage_model(self, **kwargs):
        """
        Carica e/o configura il modello LLM.
        """
        pass

    @abstractmethod
    def handle_response(self, prompt: str) -> str:
        """
        Gestisce una risposta a partire da un prompt.
        """
        pass

    def handle_error(self, error: Exception) -> None:
        """
        Gestisce gli errori sollevati dal modello o durante la generazione.
        """
        logger.error(f"LLM Error: {str(error)}")
        raise LLMError(str(error))
