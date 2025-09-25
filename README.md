# Sistema de Notificação de Pedidos com RabbitMQ

Este projeto demonstra um sistema simples de notificação de status de pedidos utilizando RabbitMQ e Python. Ele é composto por dois componentes principais:

- [`Producer.py`](DS/Producer.py): Envia notificações de status de pedidos.
- [`Consumer.py`](DS/Consumer.py): Recebe e exibe notificações dos pedidos.

## Requisitos

- Python 3.x
- Biblioteca `pika`
- RabbitMQ rodando localmente (`localhost`)

## Como funciona

### [`Producer.py`](DS/Producer.py)

Este script simula o envio de notificações de status para um pedido específico (ID 123). Ele publica mensagens em uma exchange do tipo `topic` chamada `orders`, usando diferentes routing keys para cada status:

- `order.123.preparado`
- `order.123.enviado`
- `order.123.entregue`

Cada mensagem representa uma atualização do status do pedido. O envio é feito com um intervalo de 2 segundos entre cada status.

### [`Consumer.py`](DS/Consumer.py)

Este script se conecta à mesma exchange `orders` e cria uma fila temporária exclusiva para receber notificações. Ele se inscreve para receber todas as mensagens relacionadas ao pedido 123, usando o padrão de routing key `order.123.*`. Cada vez que uma mensagem é recebida, ela é exibida no console.

## Como executar

1. Certifique-se de que o RabbitMQ está rodando em sua máquina local.
2. Instale a biblioteca `pika`:
   ```sh
   pip install pika
   ```
3. Em um terminal, execute o consumidor:
   ```sh
   python Consumer.py
   ```
4. Em outro terminal, execute o produtor:
   ```sh
   python Producer.py
   ```

O consumidor irá exibir as notificações enviadas pelo produtor conforme o status do pedido muda.

## Estrutura dos arquivos

- [`Producer.py`](DS/Producer.py): Envia mensagens de status do pedido.
- [`Consumer.py`](DS/Consumer.py)