import pika
import time

# Conexão com RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criar exchange do tipo 'topic'
channel.exchange_declare(exchange='orders', exchange_type='topic')

# Receber informações do usuário
order_id = input("Digite o ID do pedido: ")

statuses_input = input("Digite os status separados por vírgula (ex: preparado,enviado,entregue): ")
statuses = [status.strip() for status in statuses_input.split(",")]

# Enviar mensagens
for status in statuses:
    routing_key = f"order.{order_id}.{status}"
    message = f"Pedido {order_id} está {status}"
    channel.basic_publish(exchange='orders', routing_key=routing_key, body=message)
    print(f"[x] Enviado: {message}")
    time.sleep(2)  # Simula tempo entre mudanças de status

connection.close()
