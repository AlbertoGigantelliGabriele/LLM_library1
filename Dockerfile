# Dockerfile

FROM python:3.12-slim

# Copia i file di progetto
WORKDIR /app
COPY . /app

# Installa dipendenze
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Esegui i test all'avvio come esempio:
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q"]
