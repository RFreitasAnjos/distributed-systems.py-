FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir pika

COPY Consumer.py .

# CMD será definido no docker-compose.yml
