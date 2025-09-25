import pika
import time
import os

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "rabbitmq")

# Conexão persistente com RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
channel = connection.channel()
channel.exchange_declare(exchange='orders', exchange_type='topic')

print("[*] Producer rodando. Digite Ctrl+C para sair.")

try:
    while True:
        # Receber informações do usuário
        order_id = input("Digite o ID do pedido: ").strip()
        if not order_id:
            print("ID do pedido inválido. Tente novamente.")
            continue

        statuses_input = input("Digite os status separados por vírgula (ex: preparado,enviado,entregue): ")
        statuses = [status.strip() for status in statuses_input.split(",") if status.strip()]
        if not statuses:
            print("Nenhum status válido fornecido. Tente novamente.")
            continue

        # Enviar mensagens
        for status in statuses:
            routing_key = f"order.{order_id}.{status}"
            message = f"Pedido {order_id} está {status}"
            channel.basic_publish(exchange='orders', routing_key=routing_key, body=message)
            print(f"[x] Enviado: {message}")
            time.sleep(1)  # opcional, para simular tempo entre status

except KeyboardInterrupt:
    print("\n[*] Encerrando Producer...")
finally:
    connection.close()
