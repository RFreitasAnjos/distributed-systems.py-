import pika
import time

# Conexão com RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criar exchange do tipo 'topic'
channel.exchange_declare(exchange='orders', exchange_type='topic')

statuses = ["preparado", "enviado", "entregue"]

order_id = 123

for status in statuses:
    routing_key = f"order.{order_id}.{status}"
    message = f"Pedido {order_id} está {status}"
    channel.basic_publish(exchange='orders', routing_key=routing_key, body=message)
    print(f"[x] Enviado: {message}")
    time.sleep(2)  # Simula tempo entre mudanças de status

connection.close()
