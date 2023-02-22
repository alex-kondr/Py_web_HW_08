import pika
from time import sleep

credentials = pika.PlainCredentials("guest", "guest")
parameters = pika.ConnectionParameters("localhost", 5672, "/", credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
# print(channel)

channel.queue_declare(queue="test")

while True:
    channel.basic_publish(exchange="", routing_key="test", body="Welcome....")
    sleep(0.01)

sleep(20)

connection.close()