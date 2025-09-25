FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir pika

# Copia o arquivo correto do contexto de build
COPY Producer.py .

# CMD será definido no docker-compose.yml
