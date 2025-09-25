FROM python:3.12-slim

WORKDIR /app

# Instala diretamente o pika
RUN pip install --no-cache-dir pika

COPY . .

# CMD é definido no docker-compose.yml
