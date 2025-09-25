import pika
import time
import os

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "rabbitmq")
ORDER_ID = os.environ.get("ORDER_ID", "123")
STATUSES = os.environ.get("STATUSES", "preparado,enviado,entregue").split(",")

connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
channel = connection.channel()
channel.exchange_declare(exchange='orders', exchange_type='topic')

for status in STATUSES:
    routing_key = f"order.{ORDER_ID}.{status}"
    message = f"Pedido {ORDER_ID} está {status}"
    channel.basic_publish(exchange='orders', routing_key=routing_key, body=message)
    print(f"[x] Enviado: {message}")
    time.sleep(2)

connection.close()
