import pika
import time
import os

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "rabbitmq")

while True:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
        break
    except pika.exceptions.AMQPConnectionError:
        print("RabbitMQ não disponível, tentando novamente em 2 segundos...")
        time.sleep(2)

channel = connection.channel()
channel.exchange_declare(exchange='orders', exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='orders', queue=queue_name, routing_key="order.123.*")

print("[*] Esperando mensagens...")
channel.basic_consume(queue=queue_name, on_message_callback=lambda ch, method, properties, body: print(body.decode()), auto_ack=True)
channel.start_consuming()
