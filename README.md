# LLM_library

LLM_library1 è una libreria Python progettata per interagire con modelli di linguaggio di grandi dimensioni (LLM) attraverso client mock per OpenAI e Anthropic.

## Prerequisiti

Assicurati di avere installato i seguenti strumenti:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup

1. **Clona il repository:**

   ```bash
   git clone https://github.com/AlbertoGigantelliGabriele/LLM_library1.git
   cd LLM_library1
   ```

2. **Costruisci l'immagine Docker:**
   ```bash
      docker-compose build
   ```

3. **Avvia i container:**
   ```bash
     docker-compose up
   ```
   
4. **In alternativa:**
   ```
   docker-compose up --build
   ```
   
Questo comando avvierà i servizi definiti in docker-compose.yml, quindi anche i test già definiti.

Struttura del Progetto (v0.1.0)
  ```bash
  LLM_library1/
  ├── Dockerfile               # File per creare l'immagine Docker
  ├── docker-compose.yml       # Configurazione dei servizi Docker
  ├── logger.py                # Implementazione di logging personalizzato
  ├── mock_client_base.py      # Classe base per i client mock (astratto)
  ├── mock_client_openai.py    # Mock client per testare OpenAI API
  ├── mock_client_anthropic.py # Mock client per testare Anthropic API
  ├── requirements.txt         # Lista di dipendenze Python del progetto
  └── test.py                  # Script di test per validare le funzionalità
  ```

Dato che il numero di file e la complessita del codice è ridotta si è deciso di non applicare un ulteriore suddivisione.

## Test Test Pydantic + Logging 

1. **Checkout alla versione 0.2.0**
   
     ```
      git checkout v0.2.0
     ```
2. **Costruisci l'immagine Docker**

    ```
    docker-compose build
    ```

3. **Avvia i container**
   
    ```
     docker-compose up
    ```
   
4. **In alternativa:**
   ```
   docker-compose up --build
   ```
   
Struttura del Progetto (v0.2.0)

  ```bash
  LLM_library1/PycharmProjects/LLM_library2
  ├── Dockerfile               # File per creare l'immagine Docker
  ├── docker-compose.yml       # Configurazione dei servizi Docker
  ├── logger.py                # Implementazione di logging personalizzato
  ├── mock_client_base.py      # Classe base per i client mock (astratto)
  ├── mock_client_openai.py    # Mock client per testare OpenAI API
  ├── mock_client_anthropic.py # Mock client per testare Anthropic API
  ├── requirements.txt         # Lista di dipendenze Python del progetto
  ├── validation_models.py     # Schemi validazione 
  └── test.py                  # Script di test per validare le funzionalità
  ```
