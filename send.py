import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.83.229'))
channel = connection.channel()


channel.queue_declare(queue='qwe')

channel.basic_publish(exchange='',
                      routing_key='qwe',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
