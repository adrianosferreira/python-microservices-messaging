import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='amqp', port=5672)
)

channel = connection.channel()

channel.queue_declare(queue='my-queue', durable=True)


def callback(ch, method, properties, body):
    print('received')


channel.basic_consume(
    queue='my-queue', on_message_callback=callback, auto_ack=True
)

print('waiting for messages')

channel.start_consuming()