import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='amqp', port=5672)
)

channel = connection.channel()

channel.queue_declare(queue='my-queue', durable=True)

channel.basic_publish(exchange='', routing_key='my-queue', body='hello world')

channel.close()
