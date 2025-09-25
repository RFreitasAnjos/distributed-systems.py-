import pika

def callback(ch, method, properties, body):
    print(f"[x] Notificação recebida: {body.decode()}")

# Conexão com RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()

# Declarar exchange
channel.exchange_declare(exchange='orders', exchange_type='topic')

# Criar fila temporária para receber mensagens
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

# Escutar todos os status do pedido 123
channel.queue_bind(exchange='orders', queue=queue_name, routing_key="order.123.*")

print('[*] Esperando notificações. Pressione CTRL+C para sair.')
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
