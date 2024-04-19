import json

import pika
from django.conf import settings


def send_message_to_rabbitmq(message, tg_ids):
    rabbit_url = settings.RABBITMQ_URL
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rabbitmq',
        port=5672,
        credentials=pika.PlainCredentials('admin', 'admin')
    ))
    channel = connection.channel()

    channel.queue_declare(queue='messages')

    body = {
        'tg_ids': tg_ids,
        'message': message
    }
    channel.basic_publish(exchange='', routing_key='messages', body=json.dumps(body))

    connection.close()
