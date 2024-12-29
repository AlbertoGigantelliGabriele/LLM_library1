from pydantic import BaseModel, Field

class PromptInput(BaseModel):
    prompt: str = Field(..., min_length=1, description="Il testo a cui il modello deve rispondere.")
    context: str = Field(..., min_length=1, description="Contesto aggiuntivo obbligatorio.")

class LLMResponse(BaseModel):
    response: str

class ModelConfig(BaseModel):
    model_name: str = Field(..., min_length=1, description="Nome del modello")
    version: str = Field(default="latest", description="Versione del modello (opzionale).")

